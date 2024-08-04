<template>
  <div>
    <h1>Employee Overtime</h1>
    <form @submit.prevent="calculateOvertime">
      <div>
        <label>Number of Employees: </label>
        <input type="number" v-model="numberOfEmployees" placeholder="How many employees do you have?" required>
      </div>
      <div>
        <label>Daily work hours: </label>
        <input type="number" v-model="dailyWorkHours" placeholder="How many hours does each employee work per day?" required>
      </div>
      <div>
        <label>Overtimes per week: </label>
        <input type="number" v-model="overtimesPerWeek" placeholder="How many days a week is an employee obliged to work extra?" required>
      </div>
      <div>
        <label>Hours per Overtime: </label>
        <input type="number" v-model="hoursPerOvertime" placeholder="How many hours is one overtime shift per day?" required>
      </div>
      <div>
        <label>Target Hours: </label>
        <input type="number" v-model="targetHours" placeholder="How long is this work going to take (in hours)?" required>
      </div>
      
      <button type="submit">New Hires Needed</button>
    </form>
    <div v-if="errorMessage">
      <p style="color: red">{{ errorMessage }}</p>
    </div>
    <div v-if="successMessage">
      <p style="color: green">{{ successMessage }}</p>
    </div>
  </div>
</template>
  
<script>
export default {
  data() {
    return {
      numberOfEmployees: '',
      dailyWorkHours: '',
      overtimesPerWeek: '',
      hoursPerOvertime: '',
      targetHours: '',
      errorMessage: '',
      successMessage: ''
    };
  },
  methods: {
    async calculateOvertime() {
      const numberOfEmployees = parseInt(this.numberOfEmployees);
      const dailyWorkHours = parseFloat(this.dailyWorkHours);
      const overtimesPerWeek = parseFloat(this.overtimesPerWeek);
      const hoursPerOvertime = parseFloat(this.hoursPerOvertime);
      const targetHours = parseFloat(this.targetHours);

      if (!numberOfEmployees || !dailyWorkHours || !overtimesPerWeek || !hoursPerOvertime || !targetHours) {
        this.errorMessage = "Please fill in all fields with valid values.";
        return;
      }

      if (numberOfEmployees <= 0 || dailyWorkHours <= 0 || overtimesPerWeek < 0 || hoursPerOvertime <= 0 || targetHours <= 0) {
        this.errorMessage = "All values must be positive numbers.";
        return;
      }

      this.errorMessage = '';

      try {
        const response = await fetch('http://127.0.0.1:5000/overtime', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            number_of_employees: numberOfEmployees,
            individual_work_hours: dailyWorkHours,
            overtime_allowed: overtimesPerWeek,
            overtime_hours: hoursPerOvertime,
            total_hours: targetHours
          }),
        });

        if (response.ok) {
          const data = await response.json();
          this.successMessage = data.message;
          this.errorMessage = '';
        } else {
          throw new Error('Failed to fetch');
        }
      } catch (error) {
        console.error('Error calculating overtime:', error);
        this.errorMessage = 'Error calculating overtime, please try again later.';
      }
    }
  }
};
</script>
