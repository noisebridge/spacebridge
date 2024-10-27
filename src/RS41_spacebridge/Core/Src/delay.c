#include "stm32l4xx_hal.h"
#include "delay.h"

volatile uint8_t done;

void delay_init() {
	/* Not needed technically as HAL_Init is being called early on*/
	/* just retaining in case code breaks elsewhere */


}


/* TBD, will recreate if it really is needed */
//void _delay_us(uint16_t us, uint8_t precise) {
//  TIM_Cmd(TIM3, DISABLE);
//  TIM_SetAutoreload(TIM3, us);
//  TIM_SetCounter(TIM3, 0);
//  TIM_Cmd(TIM3, ENABLE);
//  done = 0;
//  while(!done){
//
//  }
//  TIM_Cmd(TIM3, DISABLE);
//}

inline void _delay_ms(uint32_t ms) {
  HAL_Delay(ms);
}
