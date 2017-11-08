<template>
  <div>
    <!--<el-dialog-->
    <!--:close-on-click-modal="false"-->
    <!--:close-on-press-escape="false"-->
    <!--title="第一次登陆个人信息修改"-->
    <!--:visible.sync="registerVisible"-->
    <!--width="60%"-->
    <!--:show-close="false"-->
    <!--:before-close="handleClose">-->
    <!--<infoRegister @submit="registerVisible=false" :inline='true'></infoRegister>-->
    <!--</el-dialog>-->
    <mheader></mheader>
    <!-- Page content -->
    <div class="w3-content" style="max-width:2000px;margin-top:6px">
      <div class="w3-container" style="width: 100%;min-height: 650px">
        <div class="w3-left" style="width: 200px;height: 100% ">
          <el-col :span="8">
            <h5></h5>
            <el-menu id="leftnav" default-active="4" class="el-menu-vertical-demo" @select="openPanel">

              <el-menu-item index="1">报名结果</el-menu-item>
              <el-menu-item index="2">比赛成绩</el-menu-item>
              <el-menu-item index="3">个人信息</el-menu-item>
            </el-menu>
          </el-col>
        </div>
        <div class="panel_content" style="margin-left:200px;display: block;padding-top:30px">
          <div id="view_register" class="w3-container panel "
               :style="{display:openedPanel==='1'?'inline-block':'none'}">
            <viewRegister></viewRegister>
          </div>
          <div id="view_grades" class="w3-container panel "
               :style="{display:openedPanel==='2'?'inline-block':'none'}">
            <viewGrades></viewGrades>
          </div>
          <div id="modify" class="w3-container panel" style="display: inline-block"
               :style="{display:openedPanel==='3'?'inline-block':'none'}">
            <infoRegister :inline='false' ref="info"></infoRegister>
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
               :style="{display:openedPanel==='4'?'inline-block':'none'}">
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
  import mheader from '../components/header'
  import mfooter from '../components/mfooter'
  import infoRegister from '../components/UserPage/infoRegister.vue'
  import projRegister from '../components/UserPage/projRegister.vue'
  import viewRegister from '../components/UserPage/viewRegister.vue'
  import viewGrades from '../components/UserPage/viewGrades.vue'
  export default {
    name: 'test',
    data () {
      return {
        registerVisible: true,
        imageUrl: require('../image/icon.jpg'),
        openedPanel: '0',
        applyState: JSON.stringify({ddl: 'ddl'})
      }
    },
    methods: {
      openPanel: function (index) {
        this.openedPanel = index
      },
      onFileChange (e) {
        var files = e.target.files || e.dataTransfer.files
        if (!files.length) return
        if (!/image+/.test(files[0].type)) {
          alert('请输入一张图片')
          return
        }
        var reader = new FileReader()
        reader.onload = (e) => {
          this.imageUrl = e.target.result
        }
        reader.readAsDataURL(files[0])
      },
      fileclick: function () {
        document.getElementById('filechooser').click()
        console.log(document.getElementById('filechooser'))
      },
      saveToLocal: function (key, value) {
        try {
          localStorage.setItem(key, value)
        } catch (e) {
          console.log('save to local failed')
        }
      },
      applyInfo (statechange) {
        var newmessage = ''
        for (var i = 0; i < statechange.length; i++) {
          newmessage = newmessage.concat('您在 ' + statechange[i].gametime.toDateString() + '的 ' + statechange[i].gamename + ' 比赛报名已经' + statechange[i].state + '\r')
        }
        this.$notify.info({
          title: '报名状态更新',
          offset: 300,
          message: newmessage
        })
      },
      getstate: function () {
        return localStorage.getItem('applyState')
      },
      compareState: function (news) {
        if (news === this.applyState) return null
        this.applyState = news
        return [{
          gametime: new Date(),
          gamename: 'football',
          state: '通过'
        }]
      },
      handleOpen (key, p) {
        console.log(key, p)
      },
      ajaxpoll () {
        var self = this
        setInterval(function () {
//          console.log('start')
          var newState = self.getstate()
          var change = self.compareState(newState)
          if (change !== null) {
//            console.log(change)
            self.applyInfo(change)
          }
        }, 5000)
      }
//      project_info_request (pk) {
//        this.$http.get('http://localhost:8000/api/' + pk).then((response) => {
//          var res = JSON.parse(response.bodyText)
//          console.log(res)
//          if (res.error_num === 0) {
//            this.pageInfo = res.list[0].fields
//            this.pageInfo.attend = '30'
//            this.project_pk = res.list[0].pk
//          } else {
//            this.$message.error('获取项目列表失败"')
//            console.log(res['msg'])
//          }
//        })
//      }

    },
    mounted: function () {
//      var input = document.getElementsByTagName('input')
//      console.log(input)
//      for (var i = 0; i < input.length; i++) {
//        console.log(input[i])
//        input[i].value = localStorage.getItem(input[i].name) || ''
//      }
//      var textarea = document.getElementsByTagName('textarea')
//      for (i = 0; i < textarea.length; i++) {
//        textarea[i].value = localStorage.getItem(textarea[i].name) || ''
//      }
//      this.ajaxpoll()
    },
    components: {
      'mheader': mheader,
      'mfooter': mfooter,
      'infoRegister': infoRegister,
      'projRegister': projRegister,
      'viewRegister': viewRegister,
      'viewGrades': viewGrades
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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


