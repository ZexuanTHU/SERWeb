import Vue from 'vue'
import Element from 'element-ui'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/login/Login'
import userpage from '@/components/userpage'
import CompetitionInfo from '@/components/CompetitionInfo/CompetitionInfo'
import GroupInfo from '@/components/CompetitionInfo/GroupInfo'
import Register from '@/components/register/Register'
import VueResource from 'vue-resource'
import auth from '../auth'
// import mheader from '@/components/header'
Vue.use(Router)
Vue.use(Element)
Vue.use(VueResource)

auth.checkAuth()

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
      path: '/CompetitionInfo/:pk',
      name: 'CompetitionInfo',
      component: CompetitionInfo
    },
    {
      path: '/GroupInfo/:pk',
      name: 'GroupInfo',
      component: GroupInfo
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
