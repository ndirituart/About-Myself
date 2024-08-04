<template>
  <div class="login-container">
    <h1>{{ msg }}</h1>
    <form @submit.prevent="login">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required>
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required>
      </div>
      <button type="submit">Login</button>
    </form>
    <div class="register-container">
      <p>Are you not a member?</p>
      <button><router-link to="/signupPage" class="no-underline text-black">Register </router-link></button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  props: {
    msg: {
      type: String,
      default: 'Welcome to Zemo!'
    }
  },
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      // Handle the login logic here
      console.log('Logging in with', this.username, this.password);
    }
  }
}
</script>

<style scoped>
.login-container {
  max-width: 300px;
  margin: 50px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
  text-align: center;
}
.form-group {
  margin-bottom: 15px;
}
.form-group label {
  display: block;
  margin-bottom: 5px;
}
.form-group input {
  width: 100%;
  padding: 8px;
  box-sizing: border-box;
}
button {
  padding: 10px 20px;
  background-color: #2aa8df;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
button:hover {
  background-color: #1935ec;
}
button:active{
  background-color: #5b1ed6;
}

.register-container {
  margin-top: 20px;
}
</style>
