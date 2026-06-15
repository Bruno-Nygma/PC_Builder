import { createSignal, effect } from "@just-dom/signals";
import { jd } from "../jd.config";
import { navigate } from "@just-dom/router";


export function NavbarLayout({ outlet }) {

  const [logged, setLogged] = createSignal(false)
  const token = localStorage.getItem('token')

  fetch(`${import.meta.env.VITE_API_URL}/auth/logged`, {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  })
    .then(async res => {
      const data = await res.json();
      const check_logged = data['result'];
      setLogged(check_logged ? check_logged : false);
    })

  return jd.div({ className: "drawer" }, [
    jd.input({ id: "my-drawer-2", type: "checkbox", className: "drawer-toggle" }),
    jd.div({ className: "drawer-content flex flex-col" }, [
      jd.div({ className: "navbar bg-base-300 w-full" }, [
        jd.div({ className: "flex-none lg:hidden" }, [
          jd.label(
            {
              htmlFor: "my-drawer-2",
              ariaLabel: "open sidebar",
              className: "btn btn-square btn-ghost",
            },
            [
              jd.svg(
                {
                  xmlns: "http://www.w3.org/2000/svg",
                  fill: "none",
                  viewBox: "0 0 24 24",
                  class: "inline-block h-6 w-6 stroke-current",
                },
                [
                  jd.svgPath({
                    "stroke-linecap": "round",
                    "stroke-linejoin": "round",
                    "stroke-width": "2",
                    d: "M4 6h16M4 12h16M4 18h16",
                  }),
                ]
              ),
            ]
          ),
        ]),
        jd.div({ className: "mx-2 flex-1 px-2" }, ["PC Builder"]),
        jd.div({ className: "hidden flex-none lg:block" }, [
          jd.ul({ className: "menu menu-horizontal space-x-4" }, [
            NavbarItem({ text: 'Builder', icon: 'Wrench', href: '/builder' }),
            jd.li({
              // if user is logged, 'account' is replaced by 'builds'
              ref: (el) => {
                effect(el, () => {
                  el.innerHTML = '';
                  if (logged()) {
                    el.replaceWith(
                      jd.button(
                        {
                          popovertarget: "popover-1",
                          style: "anchor-name:--anchor-1",
                        },
                        [
                          jd.lucide("User", { className: 'size-4 inline-block' }),
                          jd.span({}, ["Account"])
                        ]
                      ),
                      jd.ul(
                        {
                          className: "dropdown menu w-52 rounded-box bg-base-100 shadow-sm",
                          popover: "",
                          id: "popover-1",
                          style: "position-anchor:--anchor-1",
                        },
                        [
                          jd.li({}, [jd.a({ href: '/builds' }, ["Builds"])]),
                          jd.li({}, [jd.button({ 
                            onclick: () => {
                              localStorage.removeItem('token')
                              navigate('/builder')
                            }
                          }, ["Logout"])])
                        ]
                      )
                    )
                  }
                })
              }
            }, [
              jd.button(
                {
                  popovertarget: "popover-1",
                  style: "anchor-name:--anchor-1",
                },
                [
                  jd.lucide("User", { className: 'size-4 inline-block' }),
                  jd.span({}, ["Account"])
                ]
              ),
              jd.ul(
                {
                  className: "dropdown menu w-52 rounded-box bg-base-100 shadow-sm",
                  popover: "",
                  id: "popover-1",
                  style: "position-anchor:--anchor-1",
                },
                [
                  jd.li({}, [jd.a({ href: '/register' }, ["Register"])]),
                  jd.li({}, [jd.a({ href: '/login' }, ["Login"])])
                ]
              )
            ])
          ]),
        ]),
      ]),
      jd.div({ className: "p-4" }, [outlet]),
    ]),
    jd.div({ className: "drawer-side" }, [
      jd.label({
        htmlFor: "my-drawer-2",
        ariaLabel: "close sidebar",
        className: "drawer-overlay",
      }),
      jd.ul({ className: "menu bg-base-200 min-h-full w-80 p-4" }, [
        NavbarItem({ text: 'Builder', icon: 'Wrench', href: '/builder' }),
        jd.li({}, [jd.a({}, [" Sidebar Item 2"])]),
      ]),
    ]),
  ])

}


function NavbarItem({ text, icon, href }) {
  return jd.li({}, [
    jd.routerLink(
      ({ isExact }) => ({
        className: `${isExact ? 'bg-primary/10 text-primary' : ''}`,
        href
      }),
      [
        jd.lucide(icon, { className: 'size-4 inline-block' }),
        jd.span({}, [text])
      ]
    )
  ])
}