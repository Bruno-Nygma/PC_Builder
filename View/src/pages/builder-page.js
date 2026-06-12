import { createSignal, effect } from "@just-dom/signals";
import { jd } from "../jd.config";



export function BuilderPage() {

    const [componentsList, setComponentsList] = createSignal([])
    const [componentType, setComponentType] = createSignal()
    const [tableFields, setTableFields] = createSignal([])
    const [loading, setLoading] = createSignal(false)

    const build = []

    function Component(text, api_url, type) {
        return jd.button({
            className: "btn btn-soft btn-primary w-full max-w-1/12",
            ref: (el) => {
                effect(el, () => {
                    el.disabled = loading() ? true : false;
                })
            },
            onclick: () => {
                setLoading(true)
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
                    el.innerHTML = '';
                    for (const field in tableFields()) {
                        if (tableFields()[field] in component) {
                            el.append(jd.td({}, [`${component[tableFields()[field]]}`]))
                        }
                    };
                    el.append(jd.td({}, [
                        jd.button({
                            className: 'btn btn-primary btn-soft',
                            ref: (el) => {
                                effect(el, () => {
                                    el.disabled = loading() ? true : false
                                })
                            },
                            onclick: () => {
                                build.push(component);
                                console.log('[DEBUG] build: ', build);
                                setComponentType();
                            }
                        }, [
                            jd.lucide('Plus', { className: 'size-4' }),
                            "Add"
                        ])
                    ]));
                })
            }
        }, [])
    }

    function Table() {
        console.log(`[DEBUG] componentType: ${componentType()}`);
        return jd.div({
            className: `overflow-x-auto`,
            // ref: (el) => {
            //     effect(el, () => {
            //         if (!loading()) {
            //             el.replaceChildren(

            //             )
            //         } else {
            //             el.replaceChildren(
            //                 jd.lucide('Loader2', { className: 'animate-spin size-10' })
            //             )
            //         }
            //     })
            // }
        }, [
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
                                            // console.log(`[DEBUG] tableFields: `, tableFields());
                                            for (const attr in blueprint) {
                                                el.append(
                                                    jd.th({}, blueprint[attr])
                                                )
                                            }
                                            el.append(jd.th({}, []))
                                        })
                                        .finally(() => {
                                            setLoading(false)
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





