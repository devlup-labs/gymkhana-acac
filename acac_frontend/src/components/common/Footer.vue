<template lang="pug">
  div
    section
      v-card.elevation-0(color="blue darken-1 white--text" flat tile)
        v-row(style="{background: #000000}").justify-center
          v-col(cols="12" md="6").text-center
            v-layout(row)
              v-container.pa-8
                p ABOUT US
                p Students' Gymkhana, IIT Jodhpur is the governing body that looks after all student activities.
                   
          v-col(cols="12" md="6").text-center
            v-layout(row)
              v-container(class="white--text").pa-8
                p QUICK LINKS
                p
                  a(href="http://iitj.ac.in" class="white--text" target="_blank" style="text-decoration: none;") IIT Jodhpur
                p 
                   a(href="https://iitj.ac.in/footer/index.php?id=contact" class="white--text" target="_blank" style="text-decoration: none;") Contact Us

                p
                  a(href="http://iitj.ac.in/academics/index.php?id=academic_calendar" class="white--text" style="text-decoration: none;") Academic Calender
    v-footer(color="blue darken-2 white--text").text-center.justify-center.align-center
      h4.font-weight-regular © {{new Date().getFullYear() }} COPYRIGHT  | Made with
      v-icon(color="red").pa-1 mdi-heart
      a(href="https://devlup-labs.github.io/#/" class="white--text" style="text-decoration: none;")
        h4.font-weight-regular Devlup Labs
</template>

<script>
export default {
  name: "Footer",
};
</script>

<style scoped>
section {
  overflow: hidden;
}
</style>
