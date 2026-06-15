import { createSignal, effect } from "@just-dom/signals";
import { jd } from "../jd.config";

export function RegisterForm({ onSubmit } = {}){

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
                    'name': 'name',
                    'type': 'text',
                    'required': true,
                    'placeholder': 'Name',
                    'minlength': '3'
                })
            ]),
            jd.p({ className: 'validator-hint hidden' }, ['Name must have at least 3 characters'])
        ]),
        jd.div({}, [
            jd.label({ className: 'input validator w-full'}, [
                jd.lucide('Mail', { className: 'h-[1em] opacity-50'}),
                jd.input({
                    'name': 'surname',
                    'type': 'text',
                    'required': true,
                    'placeholder': 'Surname',
                    'minlength': '3'
                })
            ]),
            jd.p({ className: 'validator-hint hidden' }, ['Surname must have at least 3 characters'])
        ]),
        jd.div({}, [
            jd.label({ className: 'input validator w-full'}, [
                jd.lucide('User2', { className: 'h-[1em] opacity-50'}),
                jd.input({
                    'name': 'email',
                    'type': 'email',
                    'required': true,
                    'placeholder': 'mail@site.com'
                })
            ]),
            jd.p({ className: 'validator-hint hidden' }, ['Insert a valid mail'])
        ]),
        jd.div({}, [
            jd.label({ className: 'input validator w-full'}, [
                jd.lucide('KeyRound', { className: 'h-[1em] opacity-50'}),
                jd.input({
                    'name': 'password',
                    'type': 'password',
                    'required': true,
                    'placeholder': 'Password',
                    'minlength': '8',
                    'pattern': '(?=.*\\d)(?=.*[a-z])(?=.*[A-Z]).{8,}',
                    'title': 'Must be more than 8 characters, including number, lowercase letter, uppercase letter',
                    'autocomplete': false
                })
            ]),
            jd.p({ className: 'validator-hint hidden' }, [
                'Must be more than 8 characters and include:',
                jd.br(),
                'At least a number',
                jd.br(),
                'At least a lowercase letter',
                jd.br(),
                'At least an uppercase letter'
            ])
        ]),

        jd.button({
            ref: (el) => {
                effect(el, () => {
                    el.replaceChildren(
                        jd.lucide(loading() ? 'Loader2' : 'Save', { className: loading() ? 'size-4 animate-spin' : 'size-4' }),
                        'Registrati'
                    )
                })
            },
            'type': 'submit',
            className: 'btn btn-primary'
        }, [])

    ])
}