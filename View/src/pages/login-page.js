import { createSignal } from "@just-dom/signals";
import { jd } from "../jd.config";
import { navigate } from "@just-dom/router";
import { LoginForm } from "../components/login-form";

export function LoginPage(){

    return jd.div({
        className: 'flex flex-col gap-4 h-screen justify-center items-center'
    }, [
        jd.div({ className: 'card bg-base-200 shadow-sm w-96 text-center' }, [
            jd.div({ className: 'card-body' }, [    
                LoginForm({
                    onSubmit: async (e) => {
                        const formData = new FormData(e.target);
                        const data = Object.fromEntries(formData);
                        fetch(`${import.meta.env.VITE_API_URL}/auth/login`, {
                            method: 'POST',
                            body: JSON.stringify(data),
                            headers: { 
                                'Content-Type': 'application/json'
                            }
                        }).then(async res =>{
                            const data = await res.json();
                            if('token' in data){
                                localStorage.setItem('token', data['token'])
                            }
                            navigate('/builder')
                        })
                    }
                })
            ])
        ])
    ])
}