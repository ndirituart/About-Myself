import { createRouter, createWebHistory } from "vue-router";


const routes = [
    {
        path: '/',
        component: () => import('../components/HelloWorld.vue'),
        children: [
            {
                path: '/',
                component: () => import('../components/HomePage.vue')
            },
            {
                path: '/about',
                component: () => import('../components/AboutPage.vue')
            },
            {
                path: '/contact',
                component: () => import('../components/ContactUs.vue')
            },
            {
                path: '/dashboard',
                component: () => import('../components/DashboardPage.vue')
            },
            {
                path: '/loginPage',
                component: () => import('../components/Login.vue')
            },
            {
                path: '/signupPage',
                component: () => import('../components/SignupPage.vue')
            },
            {
                path: '/hiring',
                component: ()=> import ('../models/HourlyHiring.vue')
            },
            {
                path: '/customerrelations',
                component: ()=> import ('../models/customerrelations.vue')
            },
            {
                path: '/overtime',
                component: ()=> import ('../models/OverTime.vue')
            },
            {
                path: '/salespeople',
                component: ()=> import ('../models/SalesPeople.vue')
            }
        ]
    }, 
];
const router = createRouter({
    history: createWebHistory(),
    routes,
});
export default router;