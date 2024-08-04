<template>
  <div>
    <h1>About Us</h1>
    <p>We are a software company that offers financial solutions to companies:</p>
  
    <div class="container">
      <div class="box">
        <h2><a href="https://www.zemocard.com/expense" target="_blank" rel="noopener noreferrer">Expense Management</a></h2>
        <p>Zemo easily manages your business expenses with our intuitive platform.</p>
      </div>
      <div class="box">
        <h2><a href="https://www.zemocard.com/invoicing" target="_blank" rel="noopener noreferrer">Invoicing</a></h2>
        <p>Create professional invoices and get paid faster with our invoicing solution.</p>
      </div>
      <div class="box">
        <h2><a href="https://www.zemocard.com/accounting" target="_blank" rel="noopener noreferrer">Accounting</a></h2>
        <p>Simplify your financial management and stay organized with our accounting tools.</p>
      </div>
      <div class="box last-box">
        <h2><a href="https://www.zemocard.com/payroll" target="_blank" rel="noopener noreferrer">Payroll</a></h2>
        <p>Streamline your payroll management with ease.</p>
      </div>
      <div class="box last-box">
        <h2><a href="https://www.zemocard.com/cards" target="_blank" rel="noopener noreferrer">Corporate Cards</a></h2>
        <p>Coming soon. Zemo is collaborating with banks to have Visa debit and credit cards soon.</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AboutUs'
}
</script>

<style>
.container {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 20px;
}

.box {
  background-color: #fef3e9; /* Background color for the box */
  padding: 50px;
  border: 1px solid #cf6a18;
  border-radius: 10px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1); /* Shadow effect */
  transition: transform 0.3s, box-shadow 0.3s ease; /* Smooth transition for glow effect */
  width: calc(20% - 20px); /* Make each box take 20% of the width */
}

.box:hover {
  transform: scale(1.05); /* add bounce effect on hover */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); /* increase shadow effect on hover */
}

.last-box {
  margin: 0 10px; /* remove gap between last two boxes */
 align-self: center;
}

h2 {
  font-size: 18px;
  margin-bottom: 10px;
}

p {
  font-size: 16px;
  margin-top: 0;
}
</style>