import { createSignal, effect } from "@just-dom/signals";
import { jd } from "../jd.config";



export function BuilderPage() {

    const [componentsList, setComponentsList] = createSignal([])
    const [componentType, setComponentType] = createSignal()
    const [tableFields, setTableFields] = createSignal([])
    const [loading, setLoading] = createSignal(false)
    const [buildComponents, setBuildComponents] = createSignal({})

    const build = {}

    function ComponentSelector(text, api_url, type) {
        return jd.button({
            className: "btn btn-soft btn-primary w-full",
            ref: (el) => {
                effect(el, () => {
                    // el.disabled = loading() ? true : false;
                    if (componentType() === type || loading()){
                        el.disabled = true;
                    } else {
                        el.disabled = false;
                    }
                })
            },
            onclick: () => {
                setLoading(true)
                setComponentType(type)
                fetch(`${import.meta.env.VITE_API_URL}${api_url}`,{
                    method: 'POST',
                    body: JSON.stringify(build),
                    headers:{
                        'Content-type': 'application/json'
                    }
                })
                    .then(async res => {
                        const components = await res.json();
                        console.log(`[DEBUG] components:`, components)
                        setComponentsList(components)
                    })
                console.log(`[DEBUG] componentType: ${componentType()}`);
            }
        },
            [text]
        )
    }

    function ComponentDisplayer(type){
        return jd.p({
            className: 'max-w-full text-[14px]',
            ref: (el) => {
                effect(el, () => {
                    if (type in buildComponents()){
                        console.log('[DEBUG] ComponentDisplayer ', buildComponents()[type]["model"]);
                        el.replaceChildren(buildComponents()[type]["model"])
                    }
                })
            }
        }, [])
    }

    function ComponentRow({ component }) {
        // console.log('[DEBUG] component', component);
        return jd.tr({
            ref: (el) => {
                effect(el, () => {
                    el.innerHTML = '';
                    for (const field in tableFields()) {
                        if (tableFields()[field] in component) {
                            el.append(jd.td({}, [`${component[tableFields()[field]]}${tableFields()[field] == "tdp" || tableFields()[field] == "wattage" ? 'W' : ''}${tableFields()[field] == "price" ? '$' : ''}`]))
                        }
                    };
                    el.append(jd.td({}, [
                        jd.button({
                            className: 'btn btn-primary btn-soft',
                            ref: (el) => {
                                effect(el, () => {
                                    el.disabled = loading() ? true : false;
                                    if (component["type"] in build) {
                                        el.replaceChildren(
                                            jd.lucide('ArrowDownUp', { className: 'size-4' }),
                                            "Swap"
                                        )
                                    } else {
                                        el.replaceChildren(
                                            jd.lucide('Plus', { className: 'size-4' }),
                                            "Add"
                                        )
                                    }
                                })
                            },
                            onclick: () => {
                                // if(component["type"])
                                setLoading(true)
                                build[component["type"]] = component;
                                setBuildComponents({...build});
                                console.log('[DEBUG] buildComponents: ', buildComponents());
                                setLoading(false)
                            }
                        }, [])
                    ]));
                })
            }
        }, [])
    }

    function Table() {
        console.log(`[DEBUG] componentType: ${componentType()}`);
        return jd.div({ className: `overflow-x-auto` }, [
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
                                                    jd.th({}, [
                                                        blueprint[attr].split('_').map(word => word[0].toUpperCase() + word.slice(1)).join(' ')
                                                    ])
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
        jd.div({ className: 'flex justify-around w-full' }, [
            jd.div({ className: 'w-full max-w-1/12' }, [
                ComponentSelector("CPU", "/cpu/list", "cpu"),
                ComponentDisplayer("cpu")
            ]),
            jd.div({ className: 'w-full max-w-1/12' }, [
                ComponentSelector("CPU Cooler", "/cpu_cooler/list", "cpu_cooler"),
                ComponentDisplayer("cpu_cooler")
            ]),
            jd.div({ className: 'w-full max-w-1/12' }, [
                ComponentSelector("MoBo", "/mobo/list", "mobo"),
                ComponentDisplayer("mobo")
            ]),
            jd.div({ className: 'w-full max-w-1/12' }, [
                ComponentSelector("RAM", "/memory/list", "memory"),
                ComponentDisplayer("memory")
            ]),
            jd.div({ className: 'w-full max-w-1/12' }, [
                ComponentSelector("GPU", "/gpu/list", "gpu"),
                ComponentDisplayer("gpu")
            ]),
            jd.div({ className: 'w-full max-w-1/12' }, [
                ComponentSelector("Case", "/tower_case/list", "tower_case"),
                ComponentDisplayer("tower_case")
            ]),
            jd.div({ className: 'w-full max-w-1/12' }, [
                ComponentSelector("Storage", "/storage/list", "storage"),
                ComponentDisplayer("storage")
            ]),
            jd.div({ className: 'w-full max-w-1/12' }, [
                ComponentSelector("PSU", "/psu/list", "psu"),
                ComponentDisplayer("psu")
            ])
            
        ]),
        Table()
    ])


}





