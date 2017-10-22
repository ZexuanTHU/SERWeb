<template>
  <div id="CompetitionInfo">
    <div id="nav">
      <el-menu theme="dark" :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item index="1">首页</el-menu-item>
        <el-submenu index="2">
          <template slot="title">项目列表</template>
          <el-menu-item index="2-1">项目报名</el-menu-item>
          <el-menu-item index="2-2">比赛日程</el-menu-item>
        </el-submenu>
        <el-menu-item index="3"><a href="https://www.ele.me" target="_blank">历史沿革</a></el-menu-item>
        <el-menu-item index="4"><a href="https://www.ele.me" target="_blank">院系荣誉</a></el-menu-item>
        <el-menu-item index="5"><a href="https://www.ele.me" target="_blank">突出个人</a></el-menu-item>
        <el-menu-item index="6"><a href="https://www.ele.me" target="_blank">加入院队</a></el-menu-item>
        <el-menu-item id="login" index="7">
          <router-link to="Login">用户信息</router-link>
        </el-menu-item>
      </el-menu>
    </div>

    <div id="compinfo">
      <h1 align="left">赛事资讯</h1>
      <div>
        <div align="left">
          竞赛名称:{{name}}
        </div>
        <div align="left">
          时间:{{time}}
        </div>
        <div align="left">
          地点:{{location}}
        </div>
        <div align="left">
          竞赛类别:{{catagory}}
        </div>
        <div align="left">
          主办单位:{{host}}
        </div>
        <hr>

        <h2 align="left">详细介绍</h2>
        <p>
          {{detail}}
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      name: '足球錦標賽',
      time: '12/32 14:30',
      location: '操场',
      catagory: '⚽️',
      host: '计算机系',
      detail: '足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛足球比赛'
    }
  }
}
</script>

<style>
  #compinfo{
    margin: 20px;
    text-align: left;
  }

</style>
