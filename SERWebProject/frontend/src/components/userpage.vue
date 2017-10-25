<template>
  <div>
    <!--导航栏-->
    <el-menu theme="dark" :default-active="activeIndex" class="el-menu-demo w3-top" mode="horizontal"
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
          <el-dropdown-item >注销</el-dropdown-item>
          <el-dropdown-item divided>切换账号</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </el-menu>
    <!-- Page content -->
    <div class="w3-content" style="max-width:2000px;margin-top:46px">
      <div class="w3-container" style="width: 100%;min-height: 700px">
        <div class="w3-left" style="width: 200px;height: 100% ">
          <div class="w3-card-2 w3-left leftbar"
               style="width:200px;height: 320px;margin-top: 20px;display: block;background:#d8f7fc;text-align:center;">
            <div class="w3-card" style="border: dotted 1px;background:#5d5efc;height: 20px">
            </div>
            <p v-on:click="openPanle(0,'register')" class="tablink" href="#">比赛报名</p>
            <p v-on:click="openPanle(1,'view_register')" class="tablink" href="#">报名结果</p>
            <p v-on:click="openPanle(2,'saved_event')" class="tablink">比赛收藏</p>
            <p v-on:click="openPanle(3,'modify')" class="tablink">个人信息</p>
            <p v-on:click="openPanle(4,'add_event')" class="tablink">创建比赛</p>
          </div>
        </div>
        <div class="panel_content" style="margin-left:200px;display: block; ">

          <div id="register" class="w3-container panel">
            <h1 style="font-size: large;margin: auto">regiser</h1>
          </div>
          <div id="saved_event" class="w3-container panel">
            <h1 style="font-size: large;margin: auto">saved_event</h1>
          </div>
          <div id="view_register" class="w3-container panel ">
            <h1 style="font-size: large;margin: auto">view_regiser</h1>
          </div>
          <div id="modify" class="w3-container panel" style="display: inline-block">

            <p style="margin-top: 40px"><span class="input-tag">姓名:</span> <input type="text"></p>
            <p><span class="input-tag">电话:</span> <input type="text"></p>
            <p><span class="input-tag">邮箱:</span> <input type="text"></p>
            <p><span class="input-tag" >学号:</span> <input type="text"></p>
            <p style="height: 200px"><span class="input-tag" style="vertical-align: middle">备注:</span>
              <textarea style="margin-left:10px;width: 400px;height:200px;vertical-align: middle"
                        type="text"></textarea></p>
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
          <div id="add_event" class="w3-container panel">
            <h1 style="border-bottom:2px solid #72beff;margin-left: 1em ">新比赛</h1>
            <p><span style="width: 100px">时间:</span> <input type="date"><span
              style="padding-left: 20px">地点：</span><input style="left: 500px" type="text"></p>
          </div>

        </div>
      </div>

    </div>
    <footer class="w3-container w3-padding-16 w3-center w3-opacity w3-light-grey w3-large">

      <p class="w3-medium">Powered by <a href="#" target="_blank">软件工程GROUPCHAT</a></p>
    </footer>
  </div>

</template>

<script>
  export default {
    name: 'test',
    data () {
      return {
        te:false,
        msg: 'Welcome to Your Vue.js App',
        imageUrl:require('../image/icon.jpg')
//        panle:[
//          {title:''},
//          {title:},
//        ]

      }
    }
    , methods: {
      openPanle: function openPanle (evt, option) {
        var i, x, tablinks
        x = document.getElementsByClassName('panel')
        for (i = 0; i < x.length; i++) {
          x[i].style.display = 'none'
        }
        tablinks = document.getElementsByClassName('tablink')
        for (i = 0; i < x.length; i++) {
          tablinks[i].className = tablinks[i].className.replace(' pressed', '')
        }
        document.getElementById(option).style.display = 'inline-block'
        tablinks[evt].className += ' pressed'
      },
      onFileChange(e) {
        var files = e.target.files || e.dataTransfer.files;
        if (!files.length) return;
        if(!/image+/.test(files[0].type)){
          alert('请输入一张图片');
          return;
        }
        var reader = new FileReader();

        reader.onload = (e) => {
          this.imageUrl = e.target.result;
        };
        reader.readAsDataURL(files[0]);
      },
      fileclick: function () {
        document.getElementById('filechooser').click();

      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import url("//unpkg.com/element-ui@1.4.6/lib/theme-default/index.css");
  @import "../css/w3.css";
  @import "../css/user.css";
   a{
    text-decoration: none;
  }

</style>
