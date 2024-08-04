<template>
  <div>
    <h1>Hour Based Hiring</h1>
    <form @submit.prevent="hourbased">
      <div>
        <label>Number of Employees: </label>
        <input type="number" v-model="numberOfEmployees" placeholder="How many employees are available to work on this project?" required>
      </div>
      <div>
        <label>Daily Employee Hours: </label>
        <input type="number" v-model="dailyEmployeeHours" placeholder="How many hours does each employee work per day? (0-24)" required>
      </div>
      <div>
        <label>Daily Target Hours: </label>
        <input type="number" v-model="dailyTargetHours" placeholder="How many hours do you want the work pushed per day? (0-24)" required>
      </div>
      <div>
        <label>Working Days Per Week: </label>
        <input type="number" v-model="workingDaysPerWeek" placeholder="How many days of the week are employees working? (1-7)" required>
      </div>
      <div>
        <label>Project Start: </label>
        <input type="text" v-model="projectStart" placeholder="When does your project start? (DD/MM/YY or DD/MM/YYYY)" required>
      </div>
      <div>
        <label>Project End: </label>
        <input type="text" v-model="projectEnd" placeholder="When is your project due? (DD/MM/YY or DD/MM/YYYY)" required>
      </div>
      <button type="submit">New Hires Needed</button>
    </form>
    <div v-if="message">
      <p style="color: red">{{ message }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      numberOfEmployees: '',
      dailyEmployeeHours: '',
      dailyTargetHours: '',
      workingDaysPerWeek: '',
      projectStart: '',
      projectEnd: '',
      message: ''
    };
  },
  methods: {
    parseDate(dateStr) {
      const parts = dateStr.split('/');
      if (parts.length !== 3) {
        throw new Error('Invalid date format');
      }
      const year = parts[2].length === 2 ? `20${parts[2]}` : parts[2];
      return new Date(year, parts[1] - 1, parts[0]);
    },
    validateDates() {
      this.message = '';
      try {
        const today = new Date();
        today.setHours(0, 0, 0, 0);
        const startDay = this.parseDate(this.projectStart);
        const endDay = this.parseDate(this.projectEnd);
        if (isNaN(startDay) || isNaN(endDay)) {
          throw new Error('Invalid date');
        }
        if (startDay <= today) {
          this.message = 'The start date must be after today. Please enter a valid start date.';
          return false;
        }
        if (endDay <= startDay) {
          this.message = 'The end date must be after the start date.';
          return false;
        }
        return true;
      } catch (error) {
        this.message = 'Invalid date format. Please enter the date in DD/MM/YY format.';
        return false;
      }
    },
    async hourbased() {
      const numberOfEmployees = parseInt(this.numberOfEmployees);
      const dailyEmployeeHours = parseFloat(this.dailyEmployeeHours);
      const dailyTargetHours = parseFloat(this.dailyTargetHours);
      const workingDaysPerWeek = parseFloat(this.workingDaysPerWeek);

      if (!this.validateDates()) {
        return;
      }
      //cap values at 0 or 1 and avoid invalid values
      //and calendar instead of dates input
      if (!numberOfEmployees || !dailyEmployeeHours || !dailyTargetHours || !workingDaysPerWeek) {
        this.message = "Please fill in all fields with valid values.";
        return;
      }
      if (numberOfEmployees <= 0 || dailyEmployeeHours <= 0 || dailyTargetHours <= 0 || workingDaysPerWeek <= 0) {
        this.message = "All values must be positive numbers.";
        return;
      }
      if (dailyEmployeeHours > 24 || dailyTargetHours > 24 || workingDaysPerWeek > 7) {
        this.message = "Please enter valid values for hours (0-24) and days (1-7).";
        return;
      }

      try {
        const response = await fetch('http://127.0.0.1:5000/calculate-hours', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            number_of_employees: numberOfEmployees,
            individual_work_hours: dailyEmployeeHours,
            target_work_hours: dailyTargetHours,
            individual_work_days: workingDaysPerWeek,
            start_day: this.projectStart,
            end_day: this.projectEnd
          }),
        });

        if (response.ok) {
          const data = await response.json();
          //what data we are fetching here was the message
          this.message = data.message;
        } else {
          throw new Error('Failed to fetch');
        }
      } catch (error) {
        console.error('Error calculating employees:', error);
        this.message = 'Error calculating employees, please try again later.';
      }
    }
  }
};
</script>
