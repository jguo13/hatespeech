import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Books from '../components/Books.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'Scrape',
    component: Books,
  },
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/technicalhistory",
    name: "A Brief Technical History of Scraping",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/TechnicalHistory.vue")
  },
  {
    path: "/legalhistory",
    name: "A Brief Legal History of Scraping",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/LegalHistory.vue")
  },
  {
    path: "/scrapingprojects",
    name: "A Brief History of Scraping Projects",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/ScrapingProject.vue")
  },
  {
    path: "/technicalaspects",
    name: "Technical Aspects of Scraping Projects",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/TechnicalAspects.vue")
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
