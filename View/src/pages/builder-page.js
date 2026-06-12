import { createSignal, effect } from "@just-dom/signals";
import { jd } from "../jd.config";

const [componentsList, setComponentsList] = createSignal([])
const [componentType, setComponentType] = createSignal()

export function BuilderPage() {

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

    function Table() {
        return jd.div({ className: `overflow-x-auto ${componentType() ? '' : 'hidden'}` }, [
            jd.table({ className: "table" }, [
                jd.thead({}, [
                    jd.tr({}, []),
                ]),
                jd.tbody({
                    ref: (el) => {
                        effect(el, () => {
                            el.innerHTML = '';
                            el.append(...componentsList().map(student => StudentRow({ student })));
                        })
                    }
                }, [
                    jd.tr({}, [
                        jd.td({}, [
                            jd.lucide('Loader2', { className: 'animate-spin' })
                        ])
                    ])
                ])
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



function ComponentRow({ component }) {
    return true
}

