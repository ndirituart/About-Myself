<template>
  <div>
    <header class="header">
      <nav>
        <router-link to="/dashboard" @click="toggleDashboard">≡</router-link>
        <router-link to="/contact">Contact Us</router-link>
        <router-link to="/about">About Us</router-link>
        <router-link to="/loginPage">Login</router-link>
        <router-link to="/signupPage">Sign Up</router-link>
      </nav>
    </header>
    <div class="content">
      <div class="logo">
        <img src="../assets/logo.png" alt="Logo">
      </div>
      <div class="hello">
        <h1>{{ msg }}</h1>
        <router-view />
      </div>
      <!-- Declaring the dashboard things here -->
      <div class="dashboard-overlay" v-if="showDashboard" @click.self="toggleDashboard">
        <div class="dashboard">
          <button class="close-button" @click="toggleDashboard">X</button>
          <ul>
            <li><router-link to="/hiring">Hiring</router-link></li>
            <li><router-link to="/salespeople">Sales</router-link></li>
            <li><router-link to="/overtime">Overtime</router-link></li>
            <li><router-link to="/customerrelations">Customer Relations</router-link></li>
          </ul>
        </div>
      </div>
    </div>
    <footer class="footer">
      Zemo Hiring @2024
    </footer>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      showDashboard: false
    };
  },
  methods: {
    toggleDashboard() {
      this.showDashboard = !this.showDashboard;
    }
  }
}
</script>

<style scoped>
.header {
  background-color: #2aa8df;
  color: white;
  padding: 10px 0;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000;
}
.header nav {
  text-align: center;
}
.header nav a {
  color: white;
  text-decoration: none;
  margin: 0 15px;
}
.header nav a:hover {
  text-decoration: underline;
}
.content {
  padding-top: 60px; /* Adjust this value to match the height of your header */
}
.logo {
  text-align: center;
  margin: 10px 0;
}
.logo img {
  width: 100px;  /* Make the image smaller */
  height: 50px; /* Ensure it remains circular */
  border-radius: 50%; /* Make the image circular */
  display: block;
  margin: 0 auto;
}

.dashboard-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  z-index: 1000;
  display: flex;
  align-items: flex-start;
}

.DashBoard {
  background-color: #1A1D23; /* Dark blue background for the dashboard */
  padding: 20px;
  margin: 20px 0;
  border-radius: 10px; /* Rounded corners for the dashboard container */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for a card-like effect */
}

.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 16px;
  cursor: pointer;
}
.general-button {
  padding: 10px 20px;
  background-color: #fbb03b;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.general-button:hover {
  background-color: #7cdd1a;
}

.general-button:active {
  background-color: #bc7811;
}

.footer {
  background-color: #2aa8df;
  color: white;
  text-align: center;
  padding: 10px 0;
  position: fixed;
  width: 100%;
  bottom: 0;
  z-index: 1000;
}

.hello {
  text-align: center;
  margin: 20px 0;
}

/* Added CSS for dashboard */
.DashBoard ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
}

.DashBoard ul li {
  margin: 20px 0; /* Increased margin between each item */
  width: calc(50% - 10px); /* Make each item take half the width */
}

.dashboard-link {
  text-decoration: none; /* Remove underline from links */
  color: #FFFFFF; /* White text color */
  font-size: 18px; /* Increased font size */
  font-weight: bold; /* Bold font weight */
  display: block; /* Make the link take the full width of its container */
  padding: 20px; /* Increased padding for spacing inside each item */
  border-radius: 16px; /* Rounded corners for each item */
  transition: background-color 0.3s ease, box-shadow 0.3s ease; /* Smooth transition for hover effects */
}

.dashboard-link:hover {
  background-color: #2F3438; /* Dark grey background on hover */
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Darker shadow on hover */
  color: #1DA1F2; /* Change text color on hover to Twitter's blue */
}

.dashboard-link:focus {
  color: #1DA1F2; /* Change text color when focused to Twitter's blue */
  outline: none; /* Remove default focus outline */
  box-shadow: 0 0 0 2px #1DA1F2; /* Add a blue outline on focus */
}
</style>
