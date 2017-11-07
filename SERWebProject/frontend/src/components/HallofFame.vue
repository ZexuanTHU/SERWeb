<template>
  <div>
    <mheader></mheader>
    <div class="w3-content" style="max-width:2000px;margin-top:6px">
      <div class="w3-container" style="width: 100%;min-height: 650px">
        <div class="w3-left" style="width: 200px;height: 100% ">
          <el-col :span="8">
            <h5></h5>
            <el-menu id="leftnav" default-active="4" class="el-menu-vertical-demo" @select="openPanle">

              <el-menu-item index="0">比赛报名</el-menu-item>
              <el-menu-item index="1">报名结果</el-menu-item>
              <el-menu-item index="2">比赛收藏</el-menu-item>
              <el-menu-item index="3">个人信息</el-menu-item>
              <el-menu-item index="4">创建比赛</el-menu-item>
            </el-menu>
          </el-col>
        </div>
        <div class="panel_content" style="margin-left:200px;display: block;padding-top:30px">
          <div id="register" class="w3-container panel"
               :style="{display:openedPanle==='0'?'inline-block':'none'}">
            <projRegister></projRegister>
          </div>
          <div id="view_register" class="w3-container panel "
               :style="{display:openedPanle==='1'?'inline-block':'none'}">
            <viewRegister></viewRegister>
          </div>
          <div id="saved_event" class="w3-container panel"
               :style="{display:openedPanle==='2'?'inline-block':'none'}">
            <h1 style="font-size: large;margin: auto">saved_event</h1>
          </div>
          <div id="modify" class="w3-container panel" style="display: inline-block"
               :style="{display:openedPanle==='3'?'inline-block':'none'}">
            <infoRegister :inline='false'></infoRegister>
            <div style="width: 240px;height: 360px;text-align: center;position: absolute;right: 200px;top: 40px">
              <img class="icon" :src="imageUrl"
                   style="width:100%;margin-bottom: 5px; height: 240px;border-style: solid;border-color: #e3d4d4;  border-radius: 20%;"
                   alt="">
              <button class="w3-button mboarderbtn " style="width: 50%;margin: auto;"
                      v-on:click="fileclick()">选择头像
              </button>
              <input id="filechooser" type="file" @change="onFileChange" style="display: none;"/>
            </div>
          </div>
          <div id="add_event" class="w3-container panel"
               :style="{display:openedPanle==='4'?'inline-block':'none'}">
            <h1 style="border-bottom:2px solid #72beff;margin-left: 1em ">新比赛</h1>
            <form action="" @change="saveToLocal($event.target.name,$event.target.value)">
              <p><span style="width: 100px">时间:</span> <input type="date" name="add-time">
                <span style="padding-left: 20px">地点：</span><input style="left: 500px" type="text" name="add-place"></p>
            </form>


          </div>
        </div>
      </div>
      <mfooter></mfooter>
    </div>
  </div>
</template>

<script>
  import mheader from '@/components/header'

  export default {
    components: {
      'mheader': mheader
    }
  }
</script>

<style scoped>
  @import url("//unpkg.com/element-ui@1.4.6/lib/theme-default/index.css");
  @import "../css/w3.css";
  @import "../css/user.css";

  a {
    text-decoration: none;
  }

  #leftnav {
    margin-top: 40px;
    width: 200px;
  }

</style>
