import Vue from 'vue'
import Element from 'element-ui'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import userpage from '@/components/userpage'
import CompetitionInfo from '@/components/CompetitionInfo/CompetitionInfo'
import GroupInfo from '@/components/CompetitionInfo/GroupInfo'
import HallofFame from '@/components/HallofFame'
import ProjectList from '@/components/ProjectPage'
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
      path: '/:uid',
      name: 'Hello',
      component: HelloWorld
    },
    {
      path: '/:uid/CompetitionInfo/:pid',
      name: 'CompetitionInfo',
      component: CompetitionInfo
    },
    {
      path: '/:uid/GroupInfo/:pid',
      name: 'GroupInfo',
      component: GroupInfo
    },
    {
      path: '/:uid/userpage',
      name: 'userpage',
      component: userpage
    },
    {
      path: '/:uid/HallofFame',
      name: 'HallofFame',
      component: HallofFame
    },
    {
      path: '/:uid/ProjectList',
      name: 'ProjectList',
      component: ProjectList
    }
  ]
})
