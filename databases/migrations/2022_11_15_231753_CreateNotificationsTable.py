"""CreateNotificationsTable Migration."""

from masoniteorm.migrations import Migration


class CreateNotificationsTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("Notifications") as table:
            table.increments("id")
            table.integer("user_id")
            table.string("notifiable_type")
            table.integer("notifiable_id")
            table.json("data")
            table.boolean("read")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("Notifications")
