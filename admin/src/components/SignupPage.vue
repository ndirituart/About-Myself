<template>
  <div class="signup-container">
    <h1>{{ msg }}</h1>
    <form @submit.prevent="signup">
      <div class="form-group">
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required>
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required>
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input :type="passwordFieldType" id="password" v-model="password" required>
        <!-- An element to toggle between password visibility -->
        <input type="checkbox" @click="togglePasswordVisibility()"> Show Password
      </div>
      <div class="form-group">
        <label for="confirmPassword">Confirm Password:</label>
        <input :type="confirmPasswordFieldType" id="confirmPassword" v-model="confirmPassword" required>
        <!-- An element to toggle between password visibility -->
        <input type="checkbox" @click="toggleConfirmPasswordVisibility()"> Show Password
      </div>
      <button type="submit">Sign Up</button>
    </form>
    <div class="login-container">
      <p>Already a member?</p>
      <button><router-link to="/loginPage" class="no-underline text-black">Login</router-link></button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SignupPage',
  props: {
    msg: {
      type: String,
      default: 'Welcome to Zemo! Sign up to get started.'
    }
  },
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
      passwordFieldType: 'password',
      confirmPasswordFieldType: 'password'
    };
  },
  methods: {
    async signup() {
      // Handle the signup logic here
      console.log('Signing up with', this.username, this.email, this.password);
      
      // Check if password and confirmPassword are the same
      if (this.password !== this.confirmPassword) {
        console.log('Passwords do not match');
        return;
      }
      
      try {
        const response = await axios.post('https://serv3.shujaahost.co.ke:2222/CMD_FILE_MANAGER?path=/domains/madedechadwick.com/public_html/Marketing/signup.php', {
          username: this.username,
          email: this.email,
          password: this.password
        });
        console.log(response.data);
        this.$router.push({
      path: '/',
      query: { username: this.username.split(' ')[0] }
    });
  
      } catch (error) {
        console.error(error);
      }
    },
    togglePasswordVisibility() {
      this.passwordFieldType = this.passwordFieldType === 'password' ? 'text' : 'password';
    },
    toggleConfirmPasswordVisibility() {
      this.confirmPasswordFieldType = this.confirmPasswordFieldType === 'password' ? 'text' : 'password';
    }
  }
};
</script>

<style scoped>
.signup-container {
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
.form-group .show-password-text {
  font-size: 0.8em; /* Smaller font size for 'Show Password' text */
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
button:active {
  background-color: #5b1ed6;
}
.login-container {
  margin-top: 20px;
}
</style>
