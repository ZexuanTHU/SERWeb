
import Vue from 'vue'
import Element from 'element-ui'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import userpage from '@/components/userpage'
// import CompetitionInfo from '@/components/CompetitionInfo/CompetitionInfo'
import project from '@/components/CompetitionInfo/project'
// import GroupInfo from '@/components/CompetitionInfo/GroupInfo'
import HallofFame from '@/components/HallofFame'
import ProjectList from '@/components/ProjectPage'
import SchoolTeam from '@/components/SchoolTeam'
import VueResource from 'vue-resource'
import moment from 'moment'
import auth from '../auth'
// import mheader from '@/components/header'
Vue.use(Router)
Vue.use(Element)
Vue.use(VueResource)

Vue.filter('formatDate', function (value) {
  if (value) {
    return moment(String(value)).format('YYYY/MM/DD')
  }
})

auth.checkAuth()

// noinspection JSAnnotator
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Hello_',
      component: HelloWorld
    },
    {
      path: '/HallofFame',
      name: 'HallofFame_',
      component: HallofFame
    },
    {
      path: '/ProjectList',
      name: 'ProjectList_',
      component: ProjectList
    },
    {
      path: '/SchoolTeam',
      name: 'SchoolTeam_',
      component: SchoolTeam
    },
    // {
    //   path: '/CompetitionInfo/:pid',
    //   name: 'CompetitionInfo_',
    //   component: CompetitionInfo
    // },
    // {
    //   path: '/GroupInfo/:pid',
    //   name: 'GroupInfo_',
    //   component: GroupInfo
    // },
    {
      path: '/project/:pid',
      name: 'project_',
      component: project
    },
    {
      path: '/:uid',
      name: 'Hello',
      component: HelloWorld
    },
    // {
    //   path: '/:uid/CompetitionInfo/:pid',
    //   name: 'CompetitionInfo',
    //   component: CompetitionInfo
    // },
    // {
    //   path: '/:uid/GroupInfo/:pid',
    //   name: 'GroupInfo',
    //   component: GroupInfo
    // },
    {
      path: '/:uid/project/:pid',
      name: 'project',
      component: project
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
    },
    {
      path: '/:uid/SchoolTeam',
      name: 'SchoolTeam',
      component: SchoolTeam
    }
  ]
})
