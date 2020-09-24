import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Book from '@/components/Book'
import login from '@/components/login'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/book',
      name: 'Book',
      component: Book
    },
    {
      path: "/login",
      component: () => import("@/views/login/index"),
      hidden: true,
    },
    {
      path: "/register",
      component: () => import("@/views/register/index"),
      hidden: true,
    },
  ]
})
