# bcLargeProjectileTurretPowerNeedBonus
#
# Used by:
# Ship: Tornado
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemMultiply(lambda mod: mod.item.requiresSkill("Large Projectile Turret"),
                                     "power", ship.getModifiedItemAttr("bcLargeTurretPower"))
