<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>报名系统</h2>
    <ul>
      <li><a href="http://127.0.0.1:8000/api" target="_blank">项目列表</a></li>
      <li><a href="https://forum.vuejs.org" target="_blank">项目报名</a></li>
      <li><a href="https://chat.vuejs.org" target="_blank">比赛日程</a></li>
      <li><a href="https://twitter.com/vuejs" target="_blank">用户信息</a></li>
      <br>
      <li><a href="http://vuejs-templates.github.io/webpack/" target="_blank">用户注册</a></li>
    </ul>
    <h2>马杯历史</h2>
    <ul>
      <li><a href="http://router.vuejs.org/" target="_blank">历史沿革</a></li>
      <li><a href="http://vuex.vuejs.org/" target="_blank">院系荣誉</a></li>
      <li><a href="http://vue-loader.vuejs.org/" target="_blank">突出个人</a></li>
      <li><a href="https://github.com/vuejs/awesome-vue" target="_blank">加入院队</a></li>
    </ul>
	<el-button>文字按钮</el-button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to GROUPCHAT Sports Events Registration System'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #743481;
}
</style>
