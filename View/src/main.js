import "./style.css";
import { createRoot } from "just-dom";
import { jd } from "./jd.config.js";
import { defineRoutes } from "@just-dom/router";
import { NavbarLayout } from "./layouts/navbar-layout.js";
import { DashboardPage } from "./pages/dashboard-page.js";
import { BuilderPage } from "./pages/builder-page.js";

const routes = defineRoutes([
  {
    layout: NavbarLayout,
    children:[
      { path: '/dashboard', element: DashboardPage },
      { path: '/builder', element: BuilderPage }
    ]
  }
])

createRoot(
  "app",
  jd.router(routes)
)
