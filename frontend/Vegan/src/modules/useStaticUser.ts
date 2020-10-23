let staticUser = {}

export const setStaticUser = (user: object) => {
  staticUser = user
}

export const getStaticUser = () => {
  return staticUser
}