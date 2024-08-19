<template>
  <div class="DashBoard" v-if="visible">
    <ul>
      <li><a href="#" class="dashboard-link">Hiring</a></li>
      <li><a href="#" class="dashboard-link">Sales</a></li>
      <li><a href="#" class="dashboard-link">Overtime</a></li>
      <li><a href="#" class="dashboard-link">Customer Relations</a></li>
    </ul>
  </div>
  <div class="background-overlay" v-if="visible"></div>
</template>

<script>
export default {
  name: 'DashBoard',
  props: {
    visible: {
      type: Boolean,
      required: true
    }
  }
}
</script>

<style scoped>
.DashBoard {
  position: fixed;
  top: 20px;
  left: 20px;
  width: 25%;
  background-color: #1A1D23; /* Dark blue background for the dashboard */
  padding: 20px;
  margin: 0;
  border-radius: 10px; /* Rounded corners for the dashboard container */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Subtle shadow for a card-like effect */
  z-index: 1;
}

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

.background-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(255, 255, 255, 0.5);
  z-index: 0;
}
</style>