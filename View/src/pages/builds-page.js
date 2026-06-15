import { navigate } from "@just-dom/router"
import { jd } from "../jd.config"
import { createSignal, effect } from "@just-dom/signals"

export function BuildsPage() {
    const token = localStorage.getItem('token')

    const [buildsList, setBuildsList] = createSignal([])

    if ('token') {
        fetch(`${import.meta.env.VITE_API_URL}/build/list`,{
            headers: {
                'Authorization': `Bearer ${token}`
            }
        }).then(async res => {
            const data = await res.json()
            setBuildsList(data)
        })
        return jd.div({
            className: 'grid grid-cols-3',
            ref: (el) => {
                effect(el, () => {
                    el.innerHTML = '';
                    
                    el.append(...buildsList().map((build, index) => BuildCard({ build}, index )))
                })
            }
        },[])
    }
    else {
        navigate('/builder')
    }

    function BuildCard({ build  },number) {
        return jd.div({ className: "card w-96 bg-base-100 card-lg shadow-sm" }, [
            jd.div({ className: "card-body" }, [
                jd.h2({ className: "card-title" }, [`Build No. ${number+1}`]),
                jd.p({}, [`${build[0]['manufacturer']} ${build[0]['model']}`,]),
                jd.p({}, [`${build[1]['manufacturer']} ${build[1]['model']}`,]),
                jd.p({}, [`${build[2]['manufacturer']} ${build[2]['model']}`,]),
                jd.p({}, [`${build[3]['manufacturer']} ${build[3]['model']}`,]),
                jd.p({}, [`${build[4]['manufacturer']} ${build[4]['model']}`,]),
                jd.p({}, [`${build[5]['manufacturer']} ${build[5]['model']}`,]),
                jd.p({}, [`${build[6]['manufacturer']} ${build[6]['model']}`,]),
                jd.p({}, [`${build[7]['manufacturer']} ${build[7]['model']}`,]),
                // jd.div({ className: "justify-end card-actions" }, [
                //     jd.div({ className: "btn btn-error" }, ["Remove"]),
                // ]),
            ]),
        ]);
    }
}