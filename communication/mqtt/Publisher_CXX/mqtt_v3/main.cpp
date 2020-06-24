#include "publisher.cpp"

int main(){

  const string message = "11122233341445566";

  // 初始化
  MQTT_nodeInit();
  MQTT_Publish(message);
  
  return 0;
}
