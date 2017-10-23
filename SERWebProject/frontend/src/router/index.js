import Vue from 'vue'
import Element from 'element-ui'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Login from '@/components/login/Login'
import CompetitionInfo from '@/components/CompetitionInfo/CompetitionInfo'

Vue.use(Router)
Vue.use(Element)

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
    }
  ]
})
