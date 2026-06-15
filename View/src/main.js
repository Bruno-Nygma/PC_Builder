import "./style.css";
import { createRoot } from "just-dom";
import { jd } from "./jd.config.js";
import { defineRoutes } from "@just-dom/router";
import { NavbarLayout } from "./layouts/navbar-layout.js";
import { DashboardPage } from "./pages/dashboard-page.js";
import { BuilderPage } from "./pages/builder-page.js";
import { RegisterPage } from "./pages/register-page.js";
import { LoginPage } from "./pages/login-page.js";

const routes = defineRoutes([
  {
    layout: NavbarLayout,
    children:[
      { path: '/dashboard', element: DashboardPage },
      { path: '/builder', element: BuilderPage }
    ]
  },
  { path: '/register', element: RegisterPage },
  { path: '/login', element: LoginPage}
])

createRoot(
  "app",
  jd.router(routes)
)
