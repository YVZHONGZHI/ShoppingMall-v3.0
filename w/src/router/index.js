import Vue from 'vue'
import VueRouter from 'vue-router'
import Vip from '../views/Vip.vue'
import Home from '../views/Home.vue'
import Site from '../views/Site.vue'
import Login from '../views/Login.vue'
import Errors from '../views/Errors.vue'
import Exhibit from '../views/Exhibit.vue'
import Register from '../views/Register.vue'
import Backend from '../views/backend/Backend.vue'
import GoodsDetail from '../views/GoodsDetail.vue'
import AddGoods from '../views/backend/AddGoods.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Created',
        component: Home
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/register',
        name: 'Register',
        component: Register
    },
    {
        path: '/home',
        name: 'Home',
        component: Home
    },
    {
        path: '/vip',
        name: 'Vip',
        component: Vip
    },
    {
        path: '/exhibit',
        name: 'Exhibit',
        component: Exhibit
    },
    {
        path: '/site/:username',
        name: 'Site',
        component: Site
    },
    {
        path: '/site/:username/category/:category_id',
        name: 'SiteCategory',
        component: Site
    },
    {
        path: '/site/:username/tag/:tag_id',
        name: 'SiteTag',
        component: Site
    },
    {
        path: '/site/:username/goods/:goods_id',
        name: 'GoodsDetail',
        component: GoodsDetail
    },
    {
        path: '/backend',
        name: 'Backend',
        component: Backend
    },
    {
        path: '/add_goods',
        name: 'AddGoods',
        component: AddGoods
    },
    {
        path: '*',
        name: 'Errors',
        component: Errors
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router