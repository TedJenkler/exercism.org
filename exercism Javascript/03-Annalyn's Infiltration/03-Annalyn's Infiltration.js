export function canExecuteFastAttack(knightIsAwake) {
    if(knightIsAwake) {
      return false
    }else {
      return true
    }
  }
  
  /**
   * A useful spy captures information, which they can't do if everyone's asleep.
   *
   * @param {boolean} knightIsAwake
   * @param {boolean} archerIsAwake
   * @param {boolean} prisonerIsAwake
   *
   * @returns {boolean} Whether or not you can spy on someone.
   */
  export function canSpy(knightIsAwake, archerIsAwake, prisonerIsAwake) {
    if(knightIsAwake || archerIsAwake || prisonerIsAwake) {
      return true
    }else {
      return false
    }
  }
  
  /**
   * You'll get caught by the archer if you signal while they're awake.
   *
   * @param {boolean} archerIsAwake
   * @param {boolean} prisonerIsAwake
   *
   * @returns {boolean} Whether or not you can send a signal to the prisoner.
   */
  export function canSignalPrisoner(archerIsAwake, prisonerIsAwake) {
    if(!archerIsAwake && prisonerIsAwake) {
      return true
    }else {
      return false
    }
  }
  
  /**
   * The final stage in the plan: freeing Annalyn's best friend.
   *
   * @param {boolean} knightIsAwake
   * @param {boolean} archerIsAwake
   * @param {boolean} prisonerIsAwake
   * @param {boolean} petDogIsPresent
   *
   * @returns {boolean} Whether or not you can free Annalyn's friend.
   */
  export function canFreePrisoner(
    knightIsAwake,
    archerIsAwake,
    prisonerIsAwake,
    petDogIsPresent,
  ) {
    if(archerIsAwake || (!archerIsAwake && !prisonerIsAwake && !petDogIsPresent && !knightIsAwake) || (!archerIsAwake && !prisonerIsAwake && !petDogIsPresent && knightIsAwake) || (!archerIsAwake && prisonerIsAwake && !petDogIsPresent && knightIsAwake)) {
      return false
    }else {
      return true
    }
  }