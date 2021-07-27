from app import ma


class Equipment:
    operational_device_count = 0
    device_count = 0

    def __init__(self, asset_category_id, asset_id, row_id, operation_status):
        self.asset_category_id = asset_category_id
        self.asset_id = asset_id
        self.row_id = row_id
        self.operation_status = operation_status
        # Equipment.device_count = Equipment.device_count + 1
        # Equipment.operational_device_count = self.__operational_devices()

    @classmethod
    def json_to_obj(cls, equipment_mandatory_json):
        return cls(**equipment_mandatory_json)

    @staticmethod
    def count_operational(equip_list):
        count = 0
        for obj in equip_list:
            if obj.operation_status == "Operational":
                count = count + 1
        Equipment.operational_device_count = count
        return Equipment.operational_device_count

    def __repr__(self):
        return f'Equipment asset_id: {self.asset_id}'


class EquipmentSchema(ma.Schema):
    class Meta:
        fields = ("asset_category_id", "asset_id", "row_id", "operation_status")

