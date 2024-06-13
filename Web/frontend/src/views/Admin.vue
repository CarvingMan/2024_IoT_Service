<template>
    <v-container fluid>
        <h1>
            관리자 페이지
        </h1>
        <div>
            <DoorActive></DoorActive>
            <VisitorLog></VisitorLog>
        </div>
    </v-container>
</template>

<script>
import DoorActive from '../components/DoorActive.vue';
import VisitorLog from '../components/VisitorLog.vue';
export default {
  name: 'Admin',
  components: {
    DoorActive,
    VisitorLog
  },
  data: () => ({
    //
  }),
  created(){
    this.$socket.on('emergency',(data)=>{
        alert(data.message)
    })  
  }
}
</script>
