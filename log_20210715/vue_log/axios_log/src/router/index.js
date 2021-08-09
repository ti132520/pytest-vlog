import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        redirect: '/layout'
    },
    {
        path: '/layout',
        name: 'Layout',
        component: () => import('../views/Layout'),
        children: [
            {
                path: 'testcase',
                name: 'Testcase',
                component: () => import('../views/TestCase'),
            },
          {
                path: 'task',
                name: 'Task',
                component: () => import('../views/Task'),
            },
        ]
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
