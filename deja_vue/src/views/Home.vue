<template>
  <div class="home">

      <section class="hero is-small is-primary mb-6">
          <div class="hero-body has-text-centered">
              <p class="title mb-6">
                  Welcome to DejaVue
              </p>
              <p class="subtitle">
                  The best jacket store online
              </p>
          </div>
      </section>

      <!--Display the products in multilines-->
      <div class="columns is-multiline">
          <div class="column is-12">
              <h2 class="is-size-2 has-text-centered">Latest products</h2>
          </div>

          <ProductBox
              v-for="product in latestProducts"
              v-bind:key="product.id"
              v-bind:product="product"
          />
      </div>
    
  </div>
</template>

<script>
    import axios from 'axios';

    import ProductBox from '@/components/ProductBox.vue';
    
    

    export default {
      name: 'Home',

      data() {
        return {
          latestProducts: []
        }
      },

      components: {
        ProductBox
      },

      mounted() {
        this.getLatestProducts()

      /**Set document title (All pages) */
        document.title =  'Home | Deja vue'
      },

    methods: {

      async getLatestProducts() {

        this.$store.commit('setIsLoading', true)
        await axios
          .get('/api/v1/latest_products/')
          .then(response => {
            this.latestProducts = response.data
          })
          .catch(error => {
            console.log(error)
          })
          this.$store.commit('setIsLoading', false)
      }
    }


    }
</script>


