// src/auth/index.js

// import Vue from 'vue'
import router from '../router/index'

// URL and endpoint constants
const API_URL = 'http://111.230.226.45:8888:8080/'
// const LOGIN_URL = API_URL + 'sessions/create/'
const SIGNUP_URL = API_URL + 'users/'

export default {
  user: {
    authenticated: false
  },
  login (context, creds, redirect) {
    console.log(creds)
    console.log(creds.user_id)
    localStorage.setItem('id_token', creds.username)
    localStorage.setItem('user_id', creds.user_id)
    context.user.autenticated = true
    router.replace(redirect, function () {
      window.location.reload()
    })
//    context.$http.post(LOGIN_URL, creds).then(function (response) {
//      console.log(response.data)
//      localStorage.setItem('id_token', creds.username)
//      console.log(creds.username)
//      this.user.authenticated = true
//      if (redirect) {
//        router.push(redirect)
//      }
//    }, function (response) {
    // Error
//      console.log(response.data)
//    })
//     Vue.$http.headers.common['Authorization'] = this.getAuthHeader()
  },
  signup (context, creds, redirect) {
    context.$http.post(SIGNUP_URL, creds, (data) => {
      localStorage.setItem('id_token', data.id_token)
      localStorage.setItem('access_token', data.access_token)
      this.user.authenticated = true
      if (redirect) {
        router.push(redirect)
      }
    }).error((err) => {
      context.error = err
    })
  },
  logout () {
    localStorage.removeItem('id_token')
    localStorage.removeItem('user_id')
    this.user.authenticated = false
    // delete Vue.$http.headers.common['Authorization']
  },
  checkAuth () {
    var jwt = localStorage.getItem('id_token')
    if (jwt) {
      this.user.authenticated = true
    } else {
      this.user.authenticated = false
    }
  },
  getAuthHeader () {
    return 'Bearer ' + window.localStorage.getItem('token')
  },
  test () {
    alert('yes')
  }
}
