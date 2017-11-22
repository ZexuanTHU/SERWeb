<template>
  <el-form :model="infoForm" :rules="rules" ref="ruleForm" label-width="80px" :inline="inline">
    <el-form-item label="学位" prop="degree">
      <el-select v-model="infoForm.reading_degree" placeholder="选择院系" class="mid">
        <el-option label="本科" value="BS"></el-option>
        <el-option label="硕士" value="MS"></el-option>
        <el-option label="博士" value="PhD"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="院系" prop="faculty">
      <el-input v-model="infoForm.faculty" placeholder="院系" class="mid">
      </el-input>
    </el-form-item>
    <br v-if="inline">
    <el-form-item label="班级" prop="class_id">
      <el-input v-model="infoForm.class_id" class="mid"></el-input>
    </el-form-item>
    <el-form-item label="名字" prop="name">
      <el-input v-model="infoForm.name" class="mid"></el-input>
    </el-form-item>
    <br v-if="inline">
    <el-form-item label="性别" prop="gender">
      <el-select v-model="infoForm.gender" placeholder="选择" class="min">
        <el-option label="男" value="M"></el-option>
        <el-option label="女" value="F"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="证件号码" prop="id_card">
      <el-input v-model="infoForm.id_card" class="mid"></el-input>
    </el-form-item>
    <br v-if="inline">
    <el-form-item label="学号" prop="student_id">
      <el-input v-model="infoForm.student_id" class="mid"></el-input>
    </el-form-item>
    <el-form-item prop="birth_date" label="生日">
      <el-date-picker type="date" placeholder="选择日期" v-model="infoForm.birth_date" class="mid"></el-date-picker>
    </el-form-item>
    <br v-if="inline">
    <el-form-item label="服装号码" prop="clothes_size">
      <el-select v-model="infoForm.clothes_size" placeholder="选择" class="min">
        <el-option label="XS" value="XS"></el-option>
        <el-option label="S" value="S"></el-option>
        <el-option label="M" value="M"></el-option>
        <el-option label="L" value="L"></el-option>
        <el-option label="XL" value="XL"></el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="移动电话" prop="cellphone_num">
      <el-input v-model="infoForm.cellphone_num" class="mid"></el-input>
    </el-form-item>
    <br v-if="inline">
    <el-form-item label="电子邮箱" prop="email">
      <el-input v-model="infoForm.email" class="mid"></el-input>
    </el-form-item>
    <el-form-item label="寝室" prop="dormitory">
      <el-input v-model="infoForm.dormitory" class="mid"></el-input>
    </el-form-item>
    <br v-if="inline">
    <el-form-item>
      <el-button type="primary" @click="submitForm">提交信息</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
  import ElInput from '../../../node_modules/element-ui/packages/input/src/input.vue'

  export default {
    components: {ElInput},
    data () {
      return {
        id: null,
        infoForm: {
          faculty: '',
          class_id: '',
          reading_degree: '',
          name: '',
          gender: '',
          id_card: '',
          student_id: '',
          birth_date: '',
          clothes_size: '',
          cellphone_num: '',
          email: '',
          dormitory: ''
        },
        rules: {
          name: [
            {
              trigger: 'blur',
              validator: function (rule, value, callback) {
                if (!value || value === '') {
                  callback(new Error('请输入名字'))
                } else {
                  setTimeout(function () {
                    if (value.length > 20) {
                      callback(new Error('名字不超过20个符号'))
                    } else callback()
                  }, 1000)
                }
              }
            }
          ],
          student_id: [
            {
              trigger: 'blur',
              validator: function (rule, value, callback) {
                if (value === '') {
                  callback(new Error('请输入学号'))
                } else {
                  setTimeout(function () {
                    var pattern = /^[0-9]{10}$/g
                    if (!pattern.test(value)) {
                      callback(new Error('学号为10个数字'))
                    } else callback()
                  }, 1000)
                }
              }
            }
          ],
          faculty: [{
            trigger: 'blur',
            validator: function (rule, value, callback) {
              if (value === '') {
                callback(new Error('请输入院系'))
              } else {
                setTimeout(function () {
                  if (value.length > 20) {
                    callback(new Error('不超过20个字符'))
                  } else callback()
                }, 1000)
              }
            }
          }],
          id_card: [{
            trigger: 'blur',
            validator: function (rule, value, callback) {
              if (value === '') {
                callback(new Error('请输入证件号码'))
              } else {
                setTimeout(function () {
                  var pattern = /^[0-9]{0,30}$/g
                  console.log('here')
                  if (!pattern.test(value)) {
                    callback(new Error('请输入小于30个的数字'))
                  } else callback()
                }, 1000)
              }
            }
          }],
          class_id: [{
            trigger: 'blur',
            validator: function (rule, value, callback) {
              if (value === '') {
                callback(new Error('请输入身份证号码'))
              } else {
                setTimeout(function () {
//                  var pattern = /^[0-9]{18}$/g
                  if (value.length > 20) {
                    callback(new Error('不超过20个字符'))
                  } else callback()
                }, 1000)
              }
            }
          }],
          reading_degree: [{
            trigger: 'blur',
            validator: function (rule, value, callback) {
              if (value === '') {
                callback(new Error('选择学位'))
              } else {
                setTimeout(function () {
                  callback()
                }, 1000)
              }
            }
          }],
          gender: [],
          birth_date: [{
            trigger: 'change',
            validator: function (rule, value, callback) {
              console.log('here', value)
              if (!value || value === '') {
                callback(new Error('请选择生日'))
              } else {
                setTimeout(function () {
                  if (new Date() < new Date(value)) {
                    callback(new Error('生日不超过当前日期'))
                  } else callback()
                }, 1000)
              }
            }
          }],
          clothes_size: [{
            trigger: 'change',
            validator: function (rule, value, callback) {
              console.log('here', value)
              if (!value || value === '') {
                callback(new Error('请选择衣服型号'))
              } else {
                setTimeout(function () {
                  callback()
                }, 1000)
              }
            }
          }],
          cellphone_num: [{
            trigger: 'blur',
            validator: function (rule, value, callback) {
              if (value === '') {
                callback(new Error('请输入手机号码'))
              } else {
                setTimeout(function () {
                  var pattern = /^[0-9]{11}$/g
                  console.log('here')
                  if (!pattern.test(value)) {
                    callback(new Error('手机号码为11个数字'))
                  } else callback()
                }, 1000)
              }
            }
          }],
          email: [{
            trigger: 'blur',
            validator: function (rule, value, callback) {
              if (value === '') {
                callback(new Error('请输入电子邮箱'))
              } else {
                setTimeout(function () {
//                  var pattern = /^\w+@/g
//                  if (!pattern.test(value)) {
//                    callback(new Error('邮箱不正确'))
//                  } else
                  callback()
                }, 1000)
              }
            }
          }],
          dormitory: [{
            trigger: 'blur',
            validator: function (rule, value, callback) {
              console.log('here', value)
              if (!value || value === '') {
                callback(new Error('请输入宿舍号'))
              } else {
                setTimeout(function () {
                  if (value.length > 20) {
                    callback(new Error('不超过20个字符'))
                  } else callback()
                }, 1000)
              }
            }
          }]

        }
      }
    },
    methods: {
      submitForm () {
//        this.$http({
//          method: 'GET',
//          url:''
//        })
        console.log(this.infoForm, 'infoForm')
        console.log(this.id, 'id')
        var self = this
        this.$refs['ruleForm'].validate(function (validate) {
          if (validate) {
            self.$http.post(
              'http://111.230.226.45:8888/api/user_info_submit/' + self.id,
              self.infoForm, {emulateJSON: true}
            ).then((response) => {
//          let res = JSON.parse(response.body)
              var res = response
              console.log('response', response)
              if (res.statusText === 'OK') {
                alert('已经提交表单')
              } else {
                alert('失败，请检查您输入')
              }
            })
            self.$emit('submit')
          } else {
            self.$message.error('信息填写错误')
          }
        })
      },
      onSubmit () {
        console.log('submit!')
      },
      storeForm () {
        console.log('store')
        localStorage.setItem('submitform', JSON.stringify(this.form))
      }
    },
    props: {
      inline: Boolean,
      uid: Number
    },
    mounted:
      function () {
        if (this.uid) {
          this.id = this.uid
        } else {
          this.id = this.$route.params.uid
        }
        this.$http.get('http://111.230.226.45:8888/api/user_info_request/' + this.id).then((response) => {
          var res = JSON.parse(response.bodyText)
          console.log(res)
          if (res.error_num === 0) {
//            this.dynamicValidateForm.name = res.list[0].fields.name
//            this.ruleForm.birth_date = ''
            this.infoForm = res.list[0].fields
          } else {
            this.$message.error('获取个人信息列表失败"')
            console.log(res['msg'])
          }
        })
      }
  }
</script>

<style scoped>
  .mid {
    width: 220px;
  }

  .min {
    width: 80px;
    margin-right: 140px;
  }
</style>
