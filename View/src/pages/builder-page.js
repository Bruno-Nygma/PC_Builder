import { createSignal, effect } from "@just-dom/signals";
import { jd } from "../jd.config";



export function BuilderPage() {

    const [componentsList, setComponentsList] = createSignal([])
    const [componentType, setComponentType] = createSignal()
    const [tableFields, setTableFields] = createSignal([])

    function Component(text, api_url, type) {
        return jd.button({
            className: "btn btn-soft btn-primary w-full max-w-1/12",
            onclick: () => {
                fetch(`${import.meta.env.VITE_API_URL}${api_url}`)
                    .then(async res => {
                        const components = await res.json();
                        console.log(`[DEBUG] components:`, components)
                        setComponentsList(components)
                    })
                setComponentType(type)
                console.log(`[DEBUG] componentType: ${componentType()}`);
            }
        },
            [text]
        )
    }

    function ComponentRow({ component }) {
        // console.log('[DEBUG] component', component);
        return jd.tr({
            ref: (el) => {
                effect(el, () => {
                    for (const field in tableFields()) {
                        if (tableFields()[field] in component) {
                            el.append(jd.td({}, [`${component[tableFields()[field]]}`]))
                        }
                    }
                    el.append(jd.td({}, [
                        jd.button({ classname: 'btn btn-primary btn-soft' }, ["Add"])
                    ]))
                })
            }
        }, [])
    }

    function Table() {
        console.log(`[DEBUG] componentType: ${componentType()}`);
        return jd.div({ className: `overflow-x-auto ` }, [ //${componentType() ? '' : 'hidden'}
            jd.table({ className: "table" }, [
                jd.thead({}, [
                    jd.tr({
                        ref: (el) => {
                            effect(el, () => {
                                if (componentType()) {
                                    el.innerHTML = '';
                                    fetch(`${import.meta.env.VITE_API_URL}/${componentType()}/blueprint`)
                                        .then(async res => {
                                            const blueprint = await res.json();
                                            setTableFields(blueprint);
                                            console.log(`[DEBUG] tableFields: `, tableFields());
                                            for (const attr in blueprint) {
                                                el.append(
                                                    jd.th({}, blueprint[attr])
                                                )
                                            }
                                        })
                                }
                            })
                        }
                    }, [])
                ]),
                jd.tbody({
                    ref: (el) => {
                        effect(el, () => {
                            el.innerHTML = '';
                            el.append(...componentsList().map(component => ComponentRow({ component })));
                        })
                    }
                }, [])
            ]),
        ]);
    }

    return jd.div({}, [
        jd.div({ className: 'flex justify-around' }, [
            Component("CPU", "/cpu/list", "cpu"),
            Component("CPU Cooler", "/cpu_cooler/list", "cpu_cooler"),
            Component("MoBo", "/mobo/list", "mobo"),
            Component("RAM", "/memory/list", "memory"),
            Component("GPU", "/gpu/list", "gpu"),
            Component("Case", "/tower_case/list", "tower_case"),
            Component("Storage", "/storage/list", "storage"),
            Component("PSU", "/psu/list", "psu")
        ]),
        Table()
    ])
}





