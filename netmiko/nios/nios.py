"""NIOS OS Support"""
from netmiko.cisco_base_connection import CiscoBaseConnection
import time

class InfobloxBase(CiscoBaseConnection):
    def session_preparation(self):
        """Prepare the session after the connection has been established."""
        self._test_channel_read(pattern=">")
        self.set_base_prompt(pattern=">")
        self.disable_paging(command="set lines 0")
        # Clear the read buffer
        time.sleep(0.3 * self.global_delay_factor)
        self.clear_buffer()

    def save_config(self, cmd="write", confirm=False, confirm_response=""):
        """Save config: write"""
        return super().save_config(
            cmd=cmd, confirm=confirm, confirm_response=confirm_response
        )


class InfobloxSSH(InfobloxBase):
    pass