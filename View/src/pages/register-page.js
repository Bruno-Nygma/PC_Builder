import { createSignal } from "@just-dom/signals";
import { RegisterForm } from "../components/register-form";
import { jd } from "../jd.config";
import { navigate } from "@just-dom/router";

export function RegisterPage(){

    return jd.div({
        className: 'flex flex-col gap-4 h-screen justify-center items-center'
    }, [
        jd.div({ className: 'card bg-base-200 shadow-sm w-96 text-center' }, [
            jd.div({ className: 'card-body' }, [    
                RegisterForm({
                    onSubmit: async (e) => {
                        const formData = new FormData(e.target);
                        const data = Object.fromEntries(formData);
                        fetch(`${import.meta.env.VITE_API_URL}/auth/register`, {
                            method: 'POST',
                            body: JSON.stringify(data),
                            headers: { 
                                'Content-Type': 'application/json'
                            }
                        }).then(async res =>{
                            const data = await res.json();
                            navigate('/builder')
                        })
                    }
                })
            ])
        ])
    ])
}