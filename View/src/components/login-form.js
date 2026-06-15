import { createSignal, effect } from "@just-dom/signals";
import { jd } from "../jd.config";

export function LoginForm({ onSubmit } = {}){

    const [loading, setLoading] = createSignal(false)
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        if (onSubmit && typeof onSubmit === 'function'){
            setLoading(true);
            await onSubmit(e);
            setLoading(false);
        }
    }

    return jd.form({ className: 'space-y-4', onsubmit: handleSubmit }, [
        jd.div({}, [
            jd.label({ className: 'input validator w-full'}, [
                jd.lucide('User2', { className: 'h-[1em] opacity-50'}),
                jd.input({
                    'name': 'email',
                    'type': 'email',
                    'required': true,
                    'placeholder': 'Email'
                })
            ])
        ]),
        jd.div({}, [
            jd.label({ className: 'input validator w-full'}, [
                jd.lucide('KeyRound', { className: 'h-[1em] opacity-50'}),
                jd.input({
                    'name': 'password',
                    'type': 'password',
                    'required': true,
                    'placeholder': 'Password',
                    'autocomplete': false
                })
            ])
        ]),

        jd.button({
            ref: (el) => {
                effect(el, () => {
                    el.replaceChildren(
                        jd.lucide(loading() ? 'Loader2' : 'Save', { className: loading() ? 'size-4 animate-spin' : 'size-4' }),
                        'Login'
                    )
                })
            },
            'type': 'submit',
            className: 'btn btn-primary'
        }, [])

    ])
}