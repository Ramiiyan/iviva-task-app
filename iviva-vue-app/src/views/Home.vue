<template>
  <v-container fluid app>
    <v-row>
      <v-col lg="4" cols="sm" class="pb-2">
        <v-card color="grey lighten-5">
          <v-row class="no-gutters">
            <div class="col-auto">
              <div class="green fill-height">&nbsp;</div>
            </div>
            <div class="col pa-3 py-4 green--text">
              <h5 class="text-truncate text-uppercase">Operational Devices</h5>
              <h1>53</h1>
            </div>
          </v-row>
        </v-card>
      </v-col>
      <v-col lg="4" cols="sm" class="pb-2">
        <v-card color="grey lighten-5">
          <v-row class="no-gutters">
            <div class="col-auto">
              <div class="red fill-height">&nbsp;</div>
            </div>
            <div class="col pa-3 py-4 red--text">
              <h5 class="text-truncate text-uppercase">Non-Operational Devices</h5>
              <h1>53</h1>
            </div>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <equip-chart></equip-chart>
    </v-row>
  </v-container>
</template>

<script>
  import EquipChart from '../components/EquipChart.vue'

  export default {
    name: 'Home',

    components: {
      EquipChart,
    },
    watch:{
      
    }
  }
</script>
