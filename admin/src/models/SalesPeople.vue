<template>
  <div>
    <h1>Marketing Individual Sale Form</h1>
    <form @submit.prevent="calculateEmployees">
      <div>
        <label>Number of Employees: </label>
        <input type="number" v-model="numberOfEmployees" placeholder="How many employees do you have?" required>
      </div>
      <div>
        <label>Individual sale: </label>
        <input type="number" v-model="individualSale" placeholder="How much does each employee bring per day?" required>
      </div>
      <div>
        <label>Monthly Target: </label>
        <input type="number" v-model="targetSales" placeholder="What is your target profit of the month?" required>
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
      individualSale: '',
      targetSales: '',
      message: ''
    };
  },
  methods: {
    async calculateEmployees() {
      const numberOfEmployees = parseInt(this.numberOfEmployees);
      const individualSale = parseFloat(this.individualSale);
      const targetSales = parseFloat(this.targetSales);

      // Ensure all inputs are provided and valid
      if (!numberOfEmployees || !individualSale || !targetSales) {
        this.message = "Please fill in all fields with valid values.";
        return;
      }

      if (numberOfEmployees <= 0 || individualSale <= 0 || targetSales <= 0) {
        this.message = "All values must be positive numbers.";
        return;
      }

      try {
        const response = await fetch('http://127.0.0.1:5000/sales', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            //your JSON string is input not output YET at this step
            number_of_employees: numberOfEmployees,
            individual_ROI: individualSale,
            total_ROI: targetSales
          }),
        });

        if (response.ok) {
          const data = await response.json();
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
