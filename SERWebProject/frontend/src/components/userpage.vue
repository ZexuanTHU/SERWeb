<template>
  <div>

    <mheader></mheader>
    <!-- Page content -->
    <div class="w3-content" style="max-width:2000px;margin-top:6px">
      <div class="w3-container" style="width: 100%;min-height: 650px">
        <div class="w3-left" style="width: 200px;height: 100% ">
          <el-col :span="8">
            <h5></h5>
            <el-menu id="leftnav" default-active="1" class="el-menu-vertical-demo" @select="openPanel">
              <el-menu-item index="1">报名结果</el-menu-item>
              <el-menu-item index="2">比赛成绩</el-menu-item>
              <el-menu-item index="3">个人信息</el-menu-item>
            </el-menu>
          </el-col>
        </div>
        <div class="panel_content" style="margin-left:200px;display: block;padding-top:30px">
          <div id="view_register" class="w3-container panel "
               :style="{display:openedPanel==='1'?'inline-block':'none'}">
            <viewRegister ref="viewRegister"></viewRegister>
          </div>
          <div id="view_grades" class="w3-container panel "
               :style="{display:openedPanel==='2'?'inline-block':'none'}">
            <viewGrades ref="viewGrades"></viewGrades>
          </div>
          <div id="modify" class="w3-container panel" style="display: inline-block"
               :style="{display:openedPanel==='3'?'inline-block':'none'}">
            <infoRegister :inline='false' ref="info"></infoRegister>
          </div>
          <div class="w3-container panel"
               :style="{display:openedPanel==='4'?'inline-block':'none'}">
            <h1 style="border-bottom:2px solid #72beff;margin-left: 1em ">新比赛</h1>
            <!--<form action="" @change="saveToLocal($event.target.name,$event.target.value)">-->
            <!--<p><span style="width: 100px">时间:</span> <input type="date" name="add-time">-->
            <!--<span style="padding-left: 20px">地点：</span><input style="left: 500px" type="text" name="add-place"></p>-->
            <!--</form>-->


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
        userProjects: 'unstart',
        openedPanel: '1',
        applyState: JSON.stringify({ddl: 'ddl'})
      }
    },
    methods: {
      openPanel: function (index) {
        this.openedPanel = index
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
      handleOpen (key, p) {
        console.log(key, p)
      },
      ajaxpoll () {
        var self = this
        setInterval(function () {
//          console.log('start')
          self.project_register_relationship_request()
        }, 5000)
      },
      project_register_relationship_request: function () {
        this.$http.get('http://localhost:8000/api/project_register_relationship_request/' + this.$route.params.uid).then((response) => {
          var res = JSON.parse(response.bodyText)
//          console.log('project_status', response)
          if (res.error_num === 0) {
            this.userProjects = res
          } else {
            this.$message.error('获取个人信息列表失败"')
            console.log(res['msg'])
          }
        })
      }

    },
    watch: {
      userProjects: function (val, oldval) {
//        console.log('val', val)
//        console.log('val', oldval)
        var refreshMessage = false
        var changedProjs = []
        try {
          if (val.list.length !== oldval.list.length || val.group_list.length !== oldval.group_list.length) {
            refreshMessage = true
          } else {
            for (var i = 0; i < val.list.length; i++) {
              if (val.list[i].fields.approval_status !== oldval.list[i].fields.approval_status) {
                console.log('haschanged')
                refreshMessage = true
                changedProjs.push(val.list[i])
              }
            }
            for (i = 0; i < val.group_list.length; i++) {
              if (val.group_list[i].fields.approval_status !== oldval.group_list[i].fields.approval_status) {
                refreshMessage = true
                changedProjs.push(val.group_list[i])
              }
            }
          }
        } catch (e) {
          console.error(e)
        }
        console.log(changedProjs, 'changedProjs')
        if (refreshMessage || oldval === 'unstart') {
          if (changedProjs.length > 0) {
            var newMessage = ''
            for (i = 0; i < changedProjs.length; i++) {
              newMessage = newMessage.concat('您在 ' + new Date(changedProjs[i].fields.register_datetime).toDateString() + '申请报名的 ' +
                (changedProjs[i].fields.registered_project_name || changedProjs[i].fields.project_name) +
                ' 比赛' + this.$refs['viewRegister'].approvalStatus(changedProjs[i].fields.approval_status) + '\r')
            }
            console.log(this.formatDate)
            this.$notify.info({
              title: '报名状态更新',
              offset: 300,
              message: newMessage,
              duration: 0
            })
          }
          var newTable = this.userProjects.list.concat(this.userProjects.group_list)
          this.$refs['viewRegister'].tableData = newTable
          this.$refs['viewGrades'].tableData = newTable
          newTable = null
        }
      }
    },
    created: function () {
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
      this.ajaxpoll()
      this.project_register_relationship_request()
      if (this.$route.params.uid && localStorage.getItem('user_id') !== this.$route.params.uid) {
        this.$router.back()
      }
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


