<!--主界面上未使用此模板-->
<template>
  <el-menu theme="dark" :default-active="activeIndex" class="el-menu-demo w3-top" mode="horizontal"
           style="position: fixed;z-index: 3"
           @select="handleSelect">
    <el-menu-item style="margin-left:10px " index="1">首页</el-menu-item>
    <el-menu-item index='3'><a href="#" target="_blank">历史沿革</a></el-menu-item>
    <el-menu-item index="4"><a href="#" target="_blank">院系荣誉</a></el-menu-item>
    <el-menu-item index="5"><a href="#" target="_blank">突出个人</a></el-menu-item>
    <el-menu-item index="6"><a href="#" target="_blank">加入院队</a></el-menu-item>
    <el-dropdown style="margin-right: 100px;float: right;margin-top: 8px">
        <span class="el-dropdown-link">
         <img class="icon" :src="imageUrl" style="width: 40px;height:40px;border-radius: 30%;" alt="">
          </span>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item>注销</el-dropdown-item>
        <el-dropdown-item divided>切换账号</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
  </el-menu>
</template>

<style scoped>
  @import url("//unpkg.com/element-ui@1.4.6/lib/theme-default/index.css");
  @import url("../css/w3.css");

  a {
    text-decoration: none;
  }
</style>

<script>
  export default {
    data () {
      return {
        imageUrl: require('../image/icon.jpg')
      }
    }
  }
</script>
