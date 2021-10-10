<template>
  <div class="text-center p-0 m-0 container-fluid">
    <Navbar />
    <div class="jumbotron m-0 jumbotron-fluid">
      <div class="container">
        <h2 class="display-4">Tax Receipt</h2>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from "@/utils/vue-imports";
import Navbar from "@/components/Navbar.vue";

@Component({
  name: "About",
  components: {
    Navbar,
  },
})
export default class About extends Vue {}
</script>
