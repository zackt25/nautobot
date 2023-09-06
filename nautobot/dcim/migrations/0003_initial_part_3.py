# Generated by Django 3.1.7 on 2021-04-01 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import nautobot.extras.models.statuses
import taggit.managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tenancy", "0001_initial"),
        ("extras", "0001_initial_part_1"),
        ("dcim", "0002_initial_part_2"),
        ("ipam", "0001_initial_part_1"),
    ]

    operations = [
        migrations.AddField(
            model_name="rackreservation",
            name="user",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name="rackgroup",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="dcim.rackgroup",
            ),
        ),
        migrations.AddField(
            model_name="rackgroup",
            name="site",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="rack_groups", to="dcim.site"
            ),
        ),
        migrations.AddField(
            model_name="rack",
            name="group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="racks",
                to="dcim.rackgroup",
            ),
        ),
        migrations.AddField(
            model_name="rack",
            name="role",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="racks",
                to="dcim.rackrole",
            ),
        ),
        migrations.AddField(
            model_name="rack",
            name="site",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="racks", to="dcim.site"),
        ),
        migrations.AddField(
            model_name="rack",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="dcim_rack_related",
                to="extras.status",
            ),
        ),
        migrations.AddField(
            model_name="rack",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="rack",
            name="tenant",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="racks",
                to="tenancy.tenant",
            ),
        ),
        migrations.AddField(
            model_name="powerporttemplate",
            name="device_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="powerporttemplates", to="dcim.devicetype"
            ),
        ),
        migrations.AddField(
            model_name="powerport",
            name="_cable_peer_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="powerport",
            name="_path",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="dcim.cablepath"
            ),
        ),
        migrations.AddField(
            model_name="powerport",
            name="cable",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to="dcim.cable"
            ),
        ),
        migrations.AddField(
            model_name="powerport",
            name="device",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="powerports", to="dcim.device"
            ),
        ),
        migrations.AddField(
            model_name="powerport",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="powerpanel",
            name="rack_group",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="dcim.rackgroup"
            ),
        ),
        migrations.AddField(
            model_name="powerpanel",
            name="site",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="dcim.site"),
        ),
        migrations.AddField(
            model_name="powerpanel",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="poweroutlettemplate",
            name="device_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="poweroutlettemplates", to="dcim.devicetype"
            ),
        ),
        migrations.AddField(
            model_name="poweroutlettemplate",
            name="power_port",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="poweroutlet_templates",
                to="dcim.powerporttemplate",
            ),
        ),
        migrations.AddField(
            model_name="poweroutlet",
            name="_cable_peer_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="poweroutlet",
            name="_path",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="dcim.cablepath"
            ),
        ),
        migrations.AddField(
            model_name="poweroutlet",
            name="cable",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to="dcim.cable"
            ),
        ),
        migrations.AddField(
            model_name="poweroutlet",
            name="device",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="poweroutlets", to="dcim.device"
            ),
        ),
        migrations.AddField(
            model_name="poweroutlet",
            name="power_port",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="poweroutlets",
                to="dcim.powerport",
            ),
        ),
        migrations.AddField(
            model_name="poweroutlet",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="powerfeed",
            name="_cable_peer_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="powerfeed",
            name="_path",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="dcim.cablepath"
            ),
        ),
        migrations.AddField(
            model_name="powerfeed",
            name="cable",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to="dcim.cable"
            ),
        ),
        migrations.AddField(
            model_name="powerfeed",
            name="power_panel",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="powerfeeds", to="dcim.powerpanel"
            ),
        ),
        migrations.AddField(
            model_name="powerfeed",
            name="rack",
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to="dcim.rack"),
        ),
        migrations.AddField(
            model_name="powerfeed",
            name="status",
            field=nautobot.extras.models.statuses.StatusField(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="dcim_powerfeed_related",
                to="extras.status",
            ),
        ),
        migrations.AddField(
            model_name="powerfeed",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="platform",
            name="manufacturer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="platforms",
                to="dcim.manufacturer",
            ),
        ),
        migrations.AddField(
            model_name="inventoryitem",
            name="device",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="inventoryitems", to="dcim.device"
            ),
        ),
        migrations.AddField(
            model_name="inventoryitem",
            name="manufacturer",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="inventory_items",
                to="dcim.manufacturer",
            ),
        ),
        migrations.AddField(
            model_name="inventoryitem",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="child_items",
                to="dcim.inventoryitem",
            ),
        ),
        migrations.AddField(
            model_name="inventoryitem",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="interfacetemplate",
            name="device_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="interfacetemplates", to="dcim.devicetype"
            ),
        ),
        migrations.AddField(
            model_name="interface",
            name="_cable_peer_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="interface",
            name="_path",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="dcim.cablepath"
            ),
        ),
        migrations.AddField(
            model_name="interface",
            name="cable",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to="dcim.cable"
            ),
        ),
        migrations.AddField(
            model_name="interface",
            name="device",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="interfaces", to="dcim.device"
            ),
        ),
        migrations.AddField(
            model_name="interface",
            name="lag",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="member_interfaces",
                to="dcim.interface",
            ),
        ),
        migrations.AddField(
            model_name="interface",
            name="tagged_vlans",
            field=models.ManyToManyField(blank=True, related_name="interfaces_as_tagged", to="ipam.VLAN"),
        ),
        migrations.AddField(
            model_name="interface",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="interface",
            name="untagged_vlan",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="interfaces_as_untagged",
                to="ipam.vlan",
            ),
        ),
        migrations.AddField(
            model_name="frontporttemplate",
            name="device_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="frontporttemplates", to="dcim.devicetype"
            ),
        ),
        migrations.AddField(
            model_name="frontporttemplate",
            name="rear_port",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="frontport_templates",
                to="dcim.rearporttemplate",
            ),
        ),
        migrations.AddField(
            model_name="frontport",
            name="_cable_peer_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="frontport",
            name="cable",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="+", to="dcim.cable"
            ),
        ),
        migrations.AddField(
            model_name="frontport",
            name="device",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="frontports", to="dcim.device"
            ),
        ),
        migrations.AddField(
            model_name="frontport",
            name="rear_port",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="frontports", to="dcim.rearport"
            ),
        ),
        migrations.AddField(
            model_name="frontport",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="devicetype",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, related_name="device_types", to="dcim.manufacturer"
            ),
        ),
        migrations.AddField(
            model_name="devicetype",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AddField(
            model_name="devicebaytemplate",
            name="device_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="devicebaytemplates", to="dcim.devicetype"
            ),
        ),
        migrations.AddField(
            model_name="devicebay",
            name="device",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="devicebays", to="dcim.device"
            ),
        ),
        migrations.AddField(
            model_name="devicebay",
            name="installed_device",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="parent_bay",
                to="dcim.device",
            ),
        ),
        migrations.AddField(
            model_name="devicebay",
            name="tags",
            field=taggit.managers.TaggableManager(through="extras.TaggedItem", to="extras.Tag"),
        ),
    ]
