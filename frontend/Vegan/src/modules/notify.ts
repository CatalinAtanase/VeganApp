import { Notify } from "quasar";

interface notificationInterface {
  type: string;
  message: string;
  timeout?: number;
  handler?: () => void
}

export const sendNotification = async ({
  type,
  message,
  timeout = 3000,
  handler = () => {}
}: notificationInterface) => {
  Notify.create({
    type,
    message,
    progress: true,
    // multiLine: true,
    timeout,
    actions: [
      {
        label: "Dismiss",
        color: "white",
        handler
      }
    ]
  });
};
