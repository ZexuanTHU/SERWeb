import Vue from 'vue'
import Element from 'element-ui'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/login/Login'
import userpage from '@/components/userpage'
import CompetitionInfo from '@/components/CompetitionInfo/CompetitionInfo'
import Register from '@/components/register/Register'
import VueResource from 'vue-resource'

Vue.use(Router)
Vue.use(Element)
Vue.use(VueResource)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello',
      component: HelloWorld
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/CompetitionInfo',
      name: 'CompetitionInfo',
      component: CompetitionInfo
    },
    {
      path: '/userpage',
      name: 'userpage',
      component: userpage
    },
    {
      path: '/Register',
      name: 'Register',
      component: Register
    }
  ]
})
