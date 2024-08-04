<template>
  <div>
    <h1>Contact Us </h1>
     
    <div class="right-pane"></div>
    <!-- Reviews Form -->
    <form @submit.prevent="submitReview">
      <div>
       <h5><label for="review">Leave a Review:</label></h5> 
        <textarea id="review" v-model="reviewText" rows="4" cols="50" placeholder="Write your review here"></textarea>
      </div>
      <button type="submit">Submit</button>
    </form>
    </div>
    
    <div class="left-pane">
      <p>Would you love to reach out to us</p>
      <p>Visit our website: </p>
      <a href=" https://zemocard.com" target="_blank" rel="noopener noreferrer">https://zemocard.com/</a>
   
    <!-- Email -->
    <div>
      <i class="fas fa-envelope"></i> <!-- FontAwesome email icon -->
      <p>Or email us at:</p>
      <a href="https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=CllgCJTLGfCrLNZFcTGqmkMmWwpQPVhNZNZGxbQpPJgCqPNTZMSQsqzzBJxZrSwGRBqPZLxfdgB">info@zemocard.com</a>
    </div>
    
    <!-- Call -->
    <div>
      <i class="fas fa-phone"></i> <!-- FontAwesome phone icon -->
      <p>You may also chat or call us on this number:</p>
      <a href="https://wa.me/254704433533">+254 704433533</a>
    </div>
    
    <!-- Location -->
    <div>
      <i class="fas fa-map-marker-alt"></i> <!-- FontAwesome location icon -->
      <span>Zemo, 331 Hillcrest Drive Karen, Nairobi Kenya</span>
    </div>
    </div>
</template>

<script>
export default {
  name: 'ContactUs',
  data() {
    return {
      reviewText: ''
    };
  },
  methods: {
    submitReview() {
      // Handle submission logic here, e.g., send review to backend or perform other actions
      console.log('Submitting review:', this.reviewText);
      // Optionally, reset the review text field after submission
      this.reviewText = '';
    }
  }
};
</script>

<style scoped>
/* Add any scoped styles here */
</style>
